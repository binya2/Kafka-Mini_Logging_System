from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, EmailStr

class UserModel(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    full_name: str = Field(..., min_length=2)
    email: EmailStr
    age: int = Field(..., ge=13, le=120)
    phone: Optional[str] = Field(default=None, min_length=9, max_length=15)
    city: Optional[str] = Field(default=None, min_length=2)
    created_at: datetime = Field(default_factory=datetime.now)
