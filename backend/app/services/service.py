from sqlalchemy.orm import Session
from ..models.userentity import User
from ..repositories import repository

class UserService:
    def get_all_users(self, db: Session) -> list[User]:
        return repository.find_all_users(db)