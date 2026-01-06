from sqlalchemy.orm import Session
from ..models.userentity import User
from ..repositories import repository
from ..schemas.user import UserCreate


class UserService:
    def get_all_users(self, db: Session) -> list[User]:
        return repository.find_all_users(db)
    
    def get_all(self, db: Session):
        return repository.find_all(db)
    
    def create_user(
            self,
            db: Session,
            data: UserCreate
            ) -> User:
        
        user = User(
            name = data.name,
            department = data.department,
            position = data.position,
            hire_date = data.hire_date
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user