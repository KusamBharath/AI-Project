import json
from datetime import date
from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.agent.graph import run_agent
from app.database import get_db
from app.schemas.interaction import InteractionCreate
from app.crud.interaction import create_interaction
import json

from app.agent.tools import (
    log_interaction_tool,
    edit_interaction_tool,
    summarize_interaction_tool,
    extract_entities_tool,
    recommend_next_action_tool,
)

router = APIRouter(
    prefix="/api/agent",
    tags=["AI Agent"]
)


class AgentRequest(BaseModel):
    message: str = Field(..., min_length=5)


class ChatLogRequest(BaseModel):
    message: str = Field(..., min_length=10)
class SummarizeRequest(BaseModel):
    notes: str


class ExtractEntitiesRequest(BaseModel):
    conversation_text: str


class RecommendActionRequest(BaseModel):
    notes: str
    sentiment: Optional[str] = "neutral"
    follow_up_required: bool = False


class LogToolRequest(BaseModel):
    hcp_name: str
    specialty: Optional[str] = None
    organization: Optional[str] = None
    interaction_type: str
    interaction_date: str
    products_discussed: Optional[str] = None
    notes: str
    sentiment: Optional[str] = "neutral"
    follow_up_required: bool = False


class EditToolRequest(BaseModel):
    interaction_id: int
    field_name: str
    new_value: str

@router.post("/ask")
def ask_agent(request: AgentRequest):
    result = run_agent(request.message)
    return result


@router.post("/chat-log")
def chat_log_interaction(
    request: ChatLogRequest,
    db: Session = Depends(get_db)
):
    from app.agent.extractor import extract_interaction_data

    extracted_data = extract_interaction_data(request.message)

    interaction_data = InteractionCreate(
        hcp_name=extracted_data["hcp_name"],
        specialty=extracted_data["specialty"],
        organization=extracted_data["organization"],
        interaction_type=extracted_data["interaction_type"],
        interaction_date=extracted_data["interaction_date"],
        products_discussed=extracted_data["products_discussed"],
        notes=extracted_data["notes"],
        ai_summary=extracted_data["ai_summary"],
        sentiment=extracted_data["sentiment"],
        samples_given=extracted_data["samples_given"],
        follow_up_required=extracted_data["follow_up_required"],
        next_follow_up_date=extracted_data["next_follow_up_date"],
        next_best_action=extracted_data["next_best_action"],
    )

    saved_interaction = create_interaction(db, interaction_data)

    return {
        "message": "Interaction logged successfully using real AI extraction",
        "extracted_data": extracted_data,
        "saved_interaction": saved_interaction
    }

@router.post("/tools/log-interaction")
def demo_log_interaction_tool(request: LogToolRequest):
    result = log_interaction_tool.invoke(request.model_dump())
    return json.loads(result)


@router.post("/tools/edit-interaction")
def demo_edit_interaction_tool(request: EditToolRequest):
    result = edit_interaction_tool.invoke(request.model_dump())
    return json.loads(result)


@router.post("/tools/summarize-interaction")
def demo_summarize_interaction_tool(request: SummarizeRequest):
    result = summarize_interaction_tool.invoke(request.model_dump())
    return json.loads(result)


@router.post("/tools/extract-entities")
def demo_extract_entities_tool(request: ExtractEntitiesRequest):
    result = extract_entities_tool.invoke(request.model_dump())
    return json.loads(result)


@router.post("/tools/recommend-next-action")
def demo_recommend_next_action_tool(request: RecommendActionRequest):
    result = recommend_next_action_tool.invoke(request.model_dump())
    return json.loads(result)