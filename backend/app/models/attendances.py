from sqlalchemy import Column, String, Integer, Date, DateTime
from sqlalchemy import Enum as SqlEnum
from ..enums.attendancesstatus import AttendancesStatus
from datetime import datetime , timezone
from ..core.db import Base

class Attendances(Base):
    __tablename__ = "attendances"
    id = Column (String(36), primary_key=True)
    user_id = Column (String(36))
    work_date = Column(Date)
    clock_in = Column(DateTime)
    clock_out = Column(DateTime)
    break_minutes = Column(Integer)
    total_work_minutes = Column(Integer)
    status = Column(
        SqlEnum(AttendancesStatus, name="attendance_status_enum")
    )
    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
        )
    
    updated_at = Column(
    DateTime(timezone=True),
    default=lambda: datetime.now(timezone.utc),
    onupdate=lambda: datetime.now(timezone.utc),
)