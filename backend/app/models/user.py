from sqlalchemy import ForeignKey, String, Integer, Date , DateTime , func , text
from sqlalchemy.orm import Mapped , mapped_column
from app.core.db import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {
    "mysql_engine": "InnoDB",
    "mysql_charset": "utf8mb4",
    "mysql_collate": "utf8mb4_unicode_ci",
}
    

    id: Mapped[str] = mapped_column(String(36), primary_key=True, server_default=text("UUID()"))
    user_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("users.id", ondelete="CASCADE"),  # ← FK + ON DELETE CASCADE
        nullable=False,
    )
    work_date: Mapped[Date]
    clock_in: Mapped[DateTime | None]
    clock_out: Mapped[DateTime | None]
    break_minutes: Mapped[int] = mapped_column(Integer, default=0)
    total_work_minutes: Mapped[int] = mapped_column(Integer, default=0)

    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    user = relationship("User", lazy="joined") # type: ignore