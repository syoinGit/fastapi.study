from sqlalchemy.orm import Session
from ..models.attendancesentitty import Attendances
from ..repositories import repository

class AttendancesService:
    def get_all_attendances(self, db:Session) -> list[Attendances]:
        return repository.find_all_attendances(db)