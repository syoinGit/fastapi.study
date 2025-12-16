from sqlalchemy import Column, String, Date, DateTime
from sqlalchemy.orm import relationship
from ..core.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String(36), primary_key=True)
    name = Column(String(50))
    department = Column(String(50))
    position = Column(String(50))
    hire_date = Column(Date)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    
    attendances = relationship(
        "Attendances",
        back_populates="user",
        cascade="all, delete-orphan"
    )