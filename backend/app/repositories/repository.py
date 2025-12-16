from sqlalchemy.orm import Session, joinedload
from ..models.userentity import User
from ..models.attendancesentitty import Attendances

def find_all_users(db: Session) -> list[User]:
    rows = db.query(User).all()
    return rows

def find_all_attendances(db: Session) -> list[Attendances]:
    rows = db.query(Attendances).all()
    return rows

def find_user_detail(db:Session) -> list[User]:
    return (
        db.query(User)
        .options(joinedload(User.attendances))
        .all()
    )

def crate_attendances(db:Session, attendance: Attendances) -> Attendances:
 db.add(attendance)
 db.commit()
 db.refresh(attendance)
 return attendance