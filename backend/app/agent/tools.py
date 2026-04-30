import json
from datetime import date
from typing import Optional

from langchain_core.tools import tool
from pydantic import BaseModel, Field


class LogInteractionInput(BaseModel):
    hcp_name: str = Field(..., description="Name of the healthcare professional")
    specialty: Optional[str] = Field(None, description="HCP specialty")
    organization: Optional[str] = Field(None, description="Hospital or clinic name")
    interaction_type: str = Field(..., description="Meeting, call, email, conference, etc.")
    interaction_date: str = Field(..., description="Date in YYYY-MM-DD format")
    products_discussed: Optional[str] = Field(None, description="Products discussed")
    notes: str = Field(..., description="Detailed interaction notes")
    sentiment: Optional[str] = Field(None, description="positive, neutral, or negative")
    follow_up_required: bool = Field(False, description="Whether follow-up is needed")


class EditInteractionInput(BaseModel):
    interaction_id: int = Field(..., description="Existing interaction ID")
    field_name: str = Field(..., description="Field to update")
    new_value: str = Field(..., description="New value for the field")


class SummarizeInteractionInput(BaseModel):
    notes: str = Field(..., description="Long interaction notes")


class ExtractEntitiesInput(BaseModel):
    conversation_text: str = Field(..., description="Natural language interaction text")


class RecommendNextActionInput(BaseModel):
    notes: str = Field(..., description="Interaction notes")
    sentiment: Optional[str] = Field(None, description="HCP sentiment")
    follow_up_required: bool = Field(False, description="Whether follow-up is required")


@tool(args_schema=LogInteractionInput)
def log_interaction_tool(
    hcp_name: str,
    specialty: Optional[str],
    organization: Optional[str],
    interaction_type: str,
    interaction_date: str,
    products_discussed: Optional[str],
    notes: str,
    sentiment: Optional[str],
    follow_up_required: bool,
) -> str:
    """
    Prepares a new HCP interaction record for database saving.
    This tool captures HCP name, specialty, organization, interaction details,
    product discussion, sentiment, and follow-up requirement.
    """
    result = {
        "tool": "log_interaction_tool",
        "action": "prepared_interaction_for_logging",
        "data": {
            "hcp_name": hcp_name,
            "specialty": specialty,
            "organization": organization,
            "interaction_type": interaction_type,
            "interaction_date": interaction_date,
            "products_discussed": products_discussed,
            "notes": notes,
            "sentiment": sentiment,
            "follow_up_required": follow_up_required,
        },
    }

    return json.dumps(result)


@tool(args_schema=EditInteractionInput)
def edit_interaction_tool(
    interaction_id: int,
    field_name: str,
    new_value: str,
) -> str:
    """
    Prepares modification instructions for an existing interaction record.
    This tool identifies which interaction and which field should be updated.
    """
    result = {
        "tool": "edit_interaction_tool",
        "action": "prepared_interaction_update",
        "data": {
            "interaction_id": interaction_id,
            "field_name": field_name,
            "new_value": new_value,
        },
    }

    return json.dumps(result)


@tool(args_schema=SummarizeInteractionInput)
def summarize_interaction_tool(notes: str) -> str:
    """
    Summarizes long HCP interaction notes into CRM-ready summary.
    """
    summary = notes.strip()

    if len(summary) > 250:
        summary = summary[:250] + "..."

    result = {
        "tool": "summarize_interaction_tool",
        "summary": summary,
    }

    return json.dumps(result)


@tool(args_schema=ExtractEntitiesInput)
def extract_entities_tool(conversation_text: str) -> str:
    """
    Extracts important CRM entities from natural language interaction text.
    """
    text = conversation_text.lower()

    sentiment = "neutral"
    if any(word in text for word in ["interested", "positive", "liked", "agreed"]):
        sentiment = "positive"
    elif any(word in text for word in ["not interested", "negative", "rejected"]):
        sentiment = "negative"

    follow_up_required = any(
        word in text for word in ["follow up", "follow-up", "next meeting", "next monday", "call again"]
    )

    result = {
        "tool": "extract_entities_tool",
        "entities": {
            "raw_text": conversation_text,
            "sentiment": sentiment,
            "follow_up_required": follow_up_required,
        },
    }

    return json.dumps(result)


@tool(args_schema=RecommendNextActionInput)
def recommend_next_action_tool(
    notes: str,
    sentiment: Optional[str],
    follow_up_required: bool,
) -> str:
    """
    Recommends the next best sales action based on HCP interest, sentiment, and follow-up requirement.
    """
    if sentiment == "positive" and follow_up_required:
        action = "Schedule a follow-up visit and share product clinical evidence."
    elif sentiment == "positive":
        action = "Send product information and maintain engagement."
    elif sentiment == "negative":
        action = "Revisit later with objection-handling material and updated evidence."
    else:
        action = "Monitor engagement and plan a light follow-up."

    result = {
        "tool": "recommend_next_action_tool",
        "next_best_action": action,
    }

    return json.dumps(result)