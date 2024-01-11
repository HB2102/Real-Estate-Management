from fastapi import APIRouter, Depends
from schemas.schemas import AdminUserDisplay, UserAuth, CityDisplay
from sqlalchemy.orm import Session
from database.database import get_db
from database_functions import db_city
from authentication import auth
from typing import List

router = APIRouter(
    tags=['Admin City'],
    prefix='/admin/city',
)


@router.post('/add_city', response_model=CityDisplay)
def admin_add_city(name: str, region_id:int ,db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_city.admin_add_city(name, region_id, db, admin.id)


@router.put('/update_city/{id}', response_model=CityDisplay)
def admin_update_city(id: int, name: str, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_city.admin_update_city(id, name, db, admin.id)


@router.delete('delete_city/{id}')
def admin_delete_city(id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_city.admin_delete_city(id, db, admin.id)


