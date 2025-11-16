from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app.core.db import get_db

from ...services import UserService, get_all_users
from ...models import User

router = APIRouter(prefix="/user", tags=["/user"])

@router.get("/getall", response_model=list[User])
def alluser(service: UserService = Depends(get_all_users),
            db: Session = Depends(get_db)
            ) -> list[User]:
    return get_all_users(db)