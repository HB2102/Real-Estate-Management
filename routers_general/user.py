from fastapi import APIRouter, Depends
from schemas.schemas import UserBase, UserAuth
from sqlalchemy.orm import Session
from database.database import get_db
from database_functions import db_user
from authentication import auth

router = APIRouter(prefix='/user', tags=['User'])


@router.post('/create')
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(request, db)


@router.get('/get_self_info')
def get_self_info(db: Session = Depends(get_db), user: UserAuth = Depends(auth.get_current_user)):
    return db_user.user_get_self_info(db, user.id)


@router.put('/update_info')
def user_update_info(request: UserBase, db: Session = Depends(get_db), user: UserAuth = Depends(auth.get_current_user)):
    return db_user.user_update_info(request, db, user.id)
