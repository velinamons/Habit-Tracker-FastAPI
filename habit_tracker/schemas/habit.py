from datetime import datetime

from pydantic import BaseModel

from habit_tracker.enums import GoalFrequency


class HabitCreate(BaseModel):
    name: str
    description: str | None = None
    goal_frequency: GoalFrequency = GoalFrequency.DAILY
    goal_count: int = 1
    is_active: bool = True


class HabitUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    goal_frequency: GoalFrequency | None = None
    goal_count: int | None = None
    is_active: bool | None = None


class HabitResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    goal_frequency: GoalFrequency = GoalFrequency.DAILY
    goal_count: int = 1
    is_active: bool = True
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True
