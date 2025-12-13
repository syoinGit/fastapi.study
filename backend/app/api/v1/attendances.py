from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.core.db import get_db
from ...services.attendancesservice import AttendancesService
from ...schemas.attendances import AttendanceBase

router = APIRouter(prefix="/attendances",tags=["attendances"])

@router.get("/getall", response_model=list[AttendanceBase])
def allattendances(
    db: Session = Depends(get_db),
    service: AttendancesService = Depends(AttendancesService),
):
    attendances = service.get_all_attendances
    print(attendances)
    
    return service.get_all_attendances(db)