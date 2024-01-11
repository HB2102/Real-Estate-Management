from fastapi import APIRouter, Depends
from schemas.schemas import AdminUserDisplay, UserAuth, UserBase
from sqlalchemy.orm import Session
from database.database import get_db
from database_functions import db_notice
from authentication import auth
from typing import List

router = APIRouter(
    tags=['Admin Notice'],
    prefix='/admin/notice',
)


@router.get('/admin_get_notice/{id}')
def admin_get_notice(id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_notice.admin_get_notice(id, db, admin.id)