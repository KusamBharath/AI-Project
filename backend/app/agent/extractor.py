import json
from datetime import date
from typing import Any, Dict

from langchain_core.messages import HumanMessage, SystemMessage

from app.agent.llm import get_llm


EXTRACTION_SYSTEM_PROMPT = """
You are an AI CRM extraction assistant for life sciences field representatives.

Extract HCP interaction details from the user's text.

Return ONLY valid JSON. Do not include markdown, explanations, or extra text.

Required JSON format:
{
  "hcp_name": "string",
  "specialty": "string",
  "organization": "string",
  "interaction_type": "string",
  "interaction_date": "YYYY-MM-DD",
  "products_discussed": "string",
  "notes": "string",
  "ai_summary": "string",
  "sentiment": "positive | neutral | negative",
  "samples_given": true,
  "follow_up_required": true,
  "next_follow_up_date": "YYYY-MM-DD or null",
  "next_best_action": "string"
}

Rules:
- If doctor name is missing, use "Unknown HCP".
- If organization is missing, use "Unknown Organization".
- If specialty is missing, use "General".
- If product is missing, use "Not specified".
- If interaction date is missing, use today's date.
- Keep ai_summary short and professional.
- next_best_action should be sales-relevant and compliant.
"""


def _safe_json_parse(content: str) -> Dict[str, Any]:
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        start = content.find("{")
        end = content.rfind("}") + 1

        if start == -1 or end == 0:
            raise ValueError("LLM did not return valid JSON")

        return json.loads(content[start:end])


def extract_interaction_data(user_message: str) -> Dict[str, Any]:
    llm = get_llm()

    today = date.today().isoformat()

    messages = [
        SystemMessage(content=EXTRACTION_SYSTEM_PROMPT),
        HumanMessage(
            content=f"""
Today's date is {today}.

User interaction note:
{user_message}
"""
        ),
    ]

    response = llm.invoke(messages)
    data = _safe_json_parse(response.content)

    data["interaction_date"] = data.get("interaction_date") or today
    data["hcp_name"] = data.get("hcp_name") or "Unknown HCP"
    data["specialty"] = data.get("specialty") or "General"
    data["organization"] = data.get("organization") or "Unknown Organization"
    data["interaction_type"] = data.get("interaction_type") or "AI Chat Log"
    data["products_discussed"] = data.get("products_discussed") or "Not specified"
    data["notes"] = data.get("notes") or user_message
    data["ai_summary"] = data.get("ai_summary") or user_message
    data["sentiment"] = data.get("sentiment") or "neutral"
    data["samples_given"] = bool(data.get("samples_given", False))
    data["follow_up_required"] = bool(data.get("follow_up_required", False))
    data["next_best_action"] = data.get("next_best_action") or "Review interaction and plan next follow-up."

    if data.get("next_follow_up_date") in ["", "null", "None"]:
        data["next_follow_up_date"] = None

    return data