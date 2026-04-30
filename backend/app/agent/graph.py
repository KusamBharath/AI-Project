from typing import Any, Dict

from langchain.agents import create_agent

from app.agent.llm import get_llm
from app.agent.prompts import SYSTEM_PROMPT
from app.agent.tools import (
    log_interaction_tool,
    edit_interaction_tool,
    summarize_interaction_tool,
    extract_entities_tool,
    recommend_next_action_tool,
)


tools = [
    log_interaction_tool,
    edit_interaction_tool,
    summarize_interaction_tool,
    extract_entities_tool,
    recommend_next_action_tool,
]


def build_agent():
    llm = get_llm()

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
    )

    return agent


agent_app = build_agent()


def run_agent(user_message: str) -> Dict[str, Any]:
    response = agent_app.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_message,
                }
            ]
        }
    )

    final_message = response["messages"][-1].content

    return {
        "input": user_message,
        "response": final_message,
    }