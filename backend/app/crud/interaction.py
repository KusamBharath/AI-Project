from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.interaction import HCPInteraction
from app.schemas.interaction import InteractionCreate, InteractionUpdate


def create_interaction(
    db: Session,
    interaction_data: InteractionCreate
) -> HCPInteraction:
    interaction = HCPInteraction(**interaction_data.model_dump())

    db.add(interaction)
    db.commit()
    db.refresh(interaction)

    return interaction


def get_interaction_by_id(
    db: Session,
    interaction_id: int
) -> Optional[HCPInteraction]:
    return (
        db.query(HCPInteraction)
        .filter(HCPInteraction.id == interaction_id)
        .first()
    )


def get_all_interactions(
    db: Session,
    skip: int = 0,
    limit: int = 100
) -> List[HCPInteraction]:
    return (
        db.query(HCPInteraction)
        .order_by(HCPInteraction.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_interaction(
    db: Session,
    interaction_id: int,
    interaction_data: InteractionUpdate
) -> Optional[HCPInteraction]:
    interaction = get_interaction_by_id(db, interaction_id)

    if not interaction:
        return None

    update_data = interaction_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(interaction, field, value)

    db.commit()
    db.refresh(interaction)

    return interaction


def delete_interaction(
    db: Session,
    interaction_id: int
) -> bool:
    interaction = get_interaction_by_id(db, interaction_id)

    if not interaction:
        return False

    db.delete(interaction)
    db.commit()

    return True