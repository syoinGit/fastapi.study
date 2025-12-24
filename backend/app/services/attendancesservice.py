from sqlalchemy.orm import Session
from ..models.attendancesentitty import Attendances
from ..repositories import repository
from ..schemas.attendance import AttendanceCreate

class AttendancesService:
    def get_all_attendances(self, db:Session) -> list[Attendances]:
        return repository.find_all_attendances(db)
    

    def create_attendances(
            self,
            db: Session,
            data: AttendanceCreate
            ) -> Attendances:

        attendance = Attendances(
            user_id=data.user_id,
            work_date=data.work_date,
            clock_in=data.clock_in,
            clock_out=data.clock_out,
            break_minutes=data.break_minutes,
            total_work_minutes=data.total_work_minutes,
            status=data.status,
        )

        db.add(attendance)
        db.commit()
        db.refresh(attendance)
        return attendance