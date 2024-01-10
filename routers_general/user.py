from fastapi import APIRouter, Depends
from schemas.schemas import UserDisplay, UserBase, UserAuth
from sqlalchemy.orm import Session
from database.database import get_db
from database_functions import db_user
from authentication import auth

router = APIRouter(prefix='/user', tags=['User'])


@router.post('/create', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(request, db)
