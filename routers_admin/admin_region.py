from fastapi import APIRouter, Depends
from schemas.schemas import UserAuth, RegionDisplay
from sqlalchemy.orm import Session
from database.database import get_db
from database_functions import db_region
from authentication import auth

router = APIRouter(
    tags=['Admin Region'],
    prefix='/admin/region',
)


@router.post('/add_region', response_model=RegionDisplay)
def admin_add_region(name: str, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_region.admin_add_region(name, db, admin.id)


@router.put('/update_region/{id}', response_model=RegionDisplay)
def admin_update_region(id: int, name: str, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_region.admin_update_region(id, name, db, admin.id)


@router.delete('delete_region/{id}')
def admin_delete_region(id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_region.admin_delete_region(id, db, admin.id)


