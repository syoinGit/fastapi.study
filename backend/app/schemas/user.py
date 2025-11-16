from datetime import date, datetime
from pydantic import BaseModel

class user(BaseModel):
    id: str
    name: str
    department: str | None = None
    position: str | None = None
    hire_date: date | None = None
    created_at: datetime
    updated_at: datetime