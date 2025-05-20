# history.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models import History, User
from utils import get_db
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()

class HistoryInput(BaseModel):
    user_id: int
    code_input: str
    code_output: str
    language: str

@router.post("/")
def save_history(item: HistoryInput, db: Session = Depends(get_db)):
    history = History(
        user_id=item.user_id,
        code_input=item.code_input,
        code_output=item.code_output,
        language=item.language,
        created_at=datetime.utcnow()
    )
    db.add(history)
    db.commit()
    return {"message": "Historia zapisana"}

@router.get("/{user_id}")
def get_history(user_id: int, db: Session = Depends(get_db)):
    return db.query(History).filter(History.user_id == user_id).all()
