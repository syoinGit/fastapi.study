from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional
from ..enums.attendancesstatus import AttendancesStatus

class AttendanceBase(BaseModel):
    user_id: str
    work_date: date

    clock_in: Optional[datetime] = None
    clock_out: Optional[datetime] = None

    break_minutes: Optional[int] = None
    total_work_minutes: Optional[int] = None

    status: AttendancesStatus


class AttendanceCreate(BaseModel):
    user_id: str
    work_date: date

    clock_in: datetime | None = None
    clock_out: datetime | None = None

    break_minutes: int | None = None
    total_work_minutes: int | None = None

    status: AttendancesStatus