from fastapi import APIRouter, Depends
from schemas.schemas import AdminUserDisplay, UserAuth, AssetTypeDisplay
from sqlalchemy.orm import Session
from database.database import get_db
from database_functions import db_asset_type
from authentication import auth
from typing import List

router = APIRouter(
    tags=['Admin Asset Type'],
    prefix='/admin/asset_type',
)


@router.post('/add_asset_type', response_model=AssetTypeDisplay)
def admin_add_city(name: str, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_asset_type.admin_add_asset_type(name, db, admin.id)


@router.put('/update_asset_type/{id}', response_model=AssetTypeDisplay)
def admin_update_asset_type(id: int, name: str, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_asset_type.admin_update_asset_type(id, name, db, admin.id)


@router.delete('delete_city/{id}')
def admin_delete_asset_type(id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_asset_type.admin_delete_asset_type(id, db, admin.id)
