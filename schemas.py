from pydantic import BaseModel
from typing import List, Optional

# -----------------------------
# TASK SCHEMAS
# -----------------------------

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True  # Pydantic v2


# -----------------------------
# USER SCHEMAS
# -----------------------------

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        from_attributes = True


# -----------------------------
# USER WITH TASKS SCHEMA
# -----------------------------

class UserWithTasks(User):
    tasks: List[Task] = []

    class Config:
        from_attributes = True
