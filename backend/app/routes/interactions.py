from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.crud.interaction import (
    create_interaction,
    get_all_interactions,
    get_interaction_by_id,
    update_interaction,
    delete_interaction,
)
from app.schemas.interaction import (
    InteractionCreate,
    InteractionUpdate,
    InteractionResponse,
)


router = APIRouter(
    prefix="/api/interactions",
    tags=["Interactions"]
)


@router.post(
    "",
    response_model=InteractionResponse,
    status_code=status.HTTP_201_CREATED
)
def create_new_interaction(
    interaction_data: InteractionCreate,
    db: Session = Depends(get_db)
):
    return create_interaction(db, interaction_data)


@router.get(
    "",
    response_model=List[InteractionResponse]
)
def list_interactions(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return get_all_interactions(db, skip, limit)


@router.get(
    "/{interaction_id}",
    response_model=InteractionResponse
)
def get_single_interaction(
    interaction_id: int,
    db: Session = Depends(get_db)
):
    interaction = get_interaction_by_id(db, interaction_id)

    if not interaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interaction not found"
        )

    return interaction


@router.put(
    "/{interaction_id}",
    response_model=InteractionResponse
)
def update_existing_interaction(
    interaction_id: int,
    interaction_data: InteractionUpdate,
    db: Session = Depends(get_db)
):
    interaction = update_interaction(db, interaction_id, interaction_data)

    if not interaction:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interaction not found"
        )

    return interaction


@router.delete(
    "/{interaction_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def remove_interaction(
    interaction_id: int,
    db: Session = Depends(get_db)
):
    is_deleted = delete_interaction(db, interaction_id)

    if not is_deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interaction not found"
        )

    return None