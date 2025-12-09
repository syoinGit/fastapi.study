from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..models.userentity import User
from dotenv import load_dotenv
import os

load_dotenv()

DB_URL = os.getenv("DB_URL")

engine = create_engine(
    f"{DB_URL}&charset=utf8mb4",
    connect_args={
        "charset": "utf8mb4",
        "use_unicode": True,
        "init_command": "SET NAMES utf8mb4"
    },
    echo=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def find_all_users(db: Session) -> list[User]:
    rows = db.query(User).all()
    return rows