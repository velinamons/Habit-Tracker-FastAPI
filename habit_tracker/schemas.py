from datetime import datetime

from pydantic import BaseModel

from habit_tracker.enums import GoalFrequency


class HabitBase(BaseModel):
    name: str
    description: str | None = None
    goal_frequency: GoalFrequency = GoalFrequency.DAILY
    goal_count: int = 1
    is_active: bool = True


class HabitCreate(HabitBase):
    pass


class HabitUpdate(BaseModel):
    name: str | None = None
    description: str | None = None
    goal_frequency: GoalFrequency | None = None
    goal_count: int | None = None
    is_active: bool | None = None


class HabitResponse(HabitBase):
    id: int
    created_at: datetime
    user_id: int

    class Config:
        orm_mode = True
