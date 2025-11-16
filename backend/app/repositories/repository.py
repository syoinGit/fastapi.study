from sqlalchemy import create_engine
from sqlalchemy.orm import session

from ..models.userEntity import User

from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")
engine = create_engine(DB_URL, echo=True)
SessionLocal = session(bind=engine)

def find_all_users(db: session) -> list[User]:
    return db.query(User).all()