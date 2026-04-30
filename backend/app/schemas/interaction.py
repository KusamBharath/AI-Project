from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, Field


class InteractionBase(BaseModel):
    hcp_name: str = Field(..., min_length=2, max_length=150)
    specialty: Optional[str] = None
    organization: Optional[str] = None

    interaction_type: str = Field(..., min_length=2, max_length=80)
    interaction_date: date

    products_discussed: Optional[str] = None
    notes: str = Field(..., min_length=5)

    ai_summary: Optional[str] = None
    sentiment: Optional[str] = None

    samples_given: bool = False
    follow_up_required: bool = False
    next_follow_up_date: Optional[date] = None

    next_best_action: Optional[str] = None


class InteractionCreate(InteractionBase):
    pass


class InteractionUpdate(BaseModel):
    hcp_name: Optional[str] = None
    specialty: Optional[str] = None
    organization: Optional[str] = None

    interaction_type: Optional[str] = None
    interaction_date: Optional[date] = None

    products_discussed: Optional[str] = None
    notes: Optional[str] = None

    ai_summary: Optional[str] = None
    sentiment: Optional[str] = None

    samples_given: Optional[bool] = None
    follow_up_required: Optional[bool] = None
    next_follow_up_date: Optional[date] = None

    next_best_action: Optional[str] = None


class InteractionResponse(InteractionBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True