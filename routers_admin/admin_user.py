from fastapi import APIRouter, Depends
from schemas.schemas import AdminUserDisplay, UserAuth, UserBase
from sqlalchemy.orm import Session
from database.database import get_db
from database_functions import db_user
from authentication import auth
from typing import List

router = APIRouter(
    tags=['Admin Accounts'],
    prefix='/admin/accounts',
)

@router.post('/create_user', response_model=AdminUserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_user.admin_create_user(request, db, admin.id)


@router.delete('/delete_user')
def admin_delete_user(user_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_user.admin_delete_user(user_id, db, admin.id)
