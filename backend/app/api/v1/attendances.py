from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.core.db import get_db
from ...services.attendancesservice import AttendancesService
from ...schemas.attendance import AttendanceBase, AttendanceCreate

router = APIRouter(prefix="/attendances",tags=["attendances"])

@router.get("/", response_model=list[AttendanceBase])
def read_allattendances(
    db: Session = Depends(get_db),
    service: AttendancesService = Depends(AttendancesService),
):
  return service.get_all_attendances(db)

@router.post("/", response_model=AttendanceBase)
def create_attendance(
  data: AttendanceCreate,
  db: Session = Depends(get_db),
  service: AttendancesService = Depends(AttendancesService),
):
  return service.create_attendances(db, data)