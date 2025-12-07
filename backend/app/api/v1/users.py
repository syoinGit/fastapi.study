from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.core.db import get_db
from ...services.service import UserService
from ...schemas.user import UserBase
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/user", tags=["user"])

@router.get("/getall")
def alluser(
    db: Session = Depends(get_db),
    service: UserService = Depends(UserService),
):
    users = service.get_all_users(db)

    data = [
        {
            "name": u.name,
            "department": u.department,
            "position": u.position,
            "hire_date": u.hire_date.isoformat() if u.hire_date else None,
        }
        for u in users
    ]

    return JSONResponse(
        content=data,
        media_type="application/json; charset=utf-8",
    )