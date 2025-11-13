from fastapi import APIRouter

from ...models.user import user
from ...services.service import serivice

router = APIRouter(prefix="/user", tags=["/user"])

@router.get("/getall", response_model=list[user])
def alluser(service) -> list[user]:
    return serivice.get_all_users()