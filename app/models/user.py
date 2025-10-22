"""User model - ready for password hashing"""
from sqlmodel import SQLModel, Field
from typing import Optional


class User(SQLModel, table=True):
    """Basic user model without auth fields"""
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True)
    username: str = Field(unique=True, index=True)
    full_name: Optional[str] = None
    is_active: bool = Field(default=True)

    # Password hashing will be added by the implementation story
    # No hashed_password field yet - to be added
