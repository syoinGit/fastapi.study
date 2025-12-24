from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.core.db import get_db
from ...services.userservice import UserService
from ...schemas.userdetail import UserDetail

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/", response_model=list[UserDetail])
def alluser(
    db: Session = Depends(get_db),
    service: UserService = Depends(UserService),
):
    return service.get_all_users(db)