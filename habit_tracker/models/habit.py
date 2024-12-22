from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from habit_tracker.db import Base
from habit_tracker.enums import GoalFrequency


class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User")

    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    goal_frequency = Column(Enum(GoalFrequency), default=GoalFrequency.DAILY, nullable=False)
    goal_count = Column(Integer, default=1, nullable=False)

    is_active = Column(Boolean, default=True, nullable=False)

