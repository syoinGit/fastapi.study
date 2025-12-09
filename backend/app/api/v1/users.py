from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.core.db import get_db
from ...services.service import UserService
from ...schemas.user import UserBase

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/getall", response_model=list[UserBase])
def alluser(
    db: Session = Depends(get_db),
    service: UserService = Depends(UserService),
):
    return service.get_all_users(db)