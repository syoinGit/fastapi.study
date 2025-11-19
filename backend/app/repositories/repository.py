from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..models.userentity import User
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def find_all_users(db: Session) -> list[User]:
    return db.query(User).all()