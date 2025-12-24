import uuid
from sqlalchemy import Column, String, Integer, Date, DateTime, Enum as SqlEnum, ForeignKey
from sqlalchemy.orm import relationship
from ..enums.attendancesstatus import AttendancesStatus
from datetime import datetime , timezone
from ..core.db import Base

class Attendances(Base):
    __tablename__ = "attendances"
    id = Column(
    String(36),
    primary_key=True,
    default=lambda: str(uuid.uuid4()),
)

    user_id = Column(
        String(36),
        ForeignKey("users.id"),
        nullable=False,
        )
    
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
    
    user = relationship("User", back_populates="attendances")