from sqlalchemy.orm import Session
from ..models.userentity import User
from ..models.attendancesentitty import Attendances

def find_all_users(db: Session) -> list[User]:
    rows = db.query(User).all()
    return rows

def find_all_attendances(db: Session) -> list[Attendances]:
    rows = db.query(Attendances).all()
    return rows