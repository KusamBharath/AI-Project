from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, Text, func

from app.database import Base


class HCPInteraction(Base):
    __tablename__ = "hcp_interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_name = Column(String(150), nullable=False, index=True)
    specialty = Column(String(120), nullable=True)
    organization = Column(String(200), nullable=True)

    interaction_type = Column(String(80), nullable=False)
    interaction_date = Column(Date, nullable=False)

    products_discussed = Column(Text, nullable=True)
    notes = Column(Text, nullable=False)

    ai_summary = Column(Text, nullable=True)
    sentiment = Column(String(50), nullable=True)

    samples_given = Column(Boolean, default=False)
    follow_up_required = Column(Boolean, default=False)
    next_follow_up_date = Column(Date, nullable=True)

    next_best_action = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )