from datetime import date, datetime
from pydantic import BaseModel, ConfigDict

# ===== Base =====
class UserBase(BaseModel):
    name: str
    department: str | None = None
    position: str | None = None
    hire_date: date | None = None

    model_config = ConfigDict(from_attributes=True)


# ===== Create (POST) =====
class UserCreate(UserBase):
    pass


# ===== Update (PUT/PATCH) =====
class UserUpdate(BaseModel):
    name: str | None = None
    department: str | None = None
    position: str | None = None
    hire_date: date | None = None


# ===== Read (GET) =====
class User(UserBase):
    id: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)