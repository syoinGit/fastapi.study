from sqlalchemy.orm import sesion
from ..repositories import repository
from ..models.userEntity import User

class UserService:
    def __init__(self, repository: repository):
        self.repository = repository

def get_all_users(self, db: sesion) -> list[User]:
    return self.repository.find_all_users(db)