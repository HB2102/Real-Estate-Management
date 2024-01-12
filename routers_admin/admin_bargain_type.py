from fastapi import APIRouter, Depends
from schemas.schemas import UserAuth, BargainTypeDisplay
from sqlalchemy.orm import Session
from database.database import get_db
from database_functions import db_bargain_type
from authentication import auth

router = APIRouter(
    tags=['Admin Bargain Type'],
    prefix='/admin/bargain_type',
)


@router.post('/add_bargain_type', response_model=BargainTypeDisplay)
def admin_add_bargain(name: str, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_bargain_type.admin_add_bargain_type(name, db, admin.id)


@router.put('/update_bargain_type/{id}', response_model=BargainTypeDisplay)
def admin_update_bargain_type(id: int, name: str, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_bargain_type.admin_update_bargain_type(id, name, db, admin.id)


@router.delete('/delete_bargain/{id}')
def admin_delete_bargain_type(id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_bargain_type.admin_delete_bargain_type(id, db, admin.id)
