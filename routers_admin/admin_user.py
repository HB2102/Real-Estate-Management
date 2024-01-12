from fastapi import APIRouter, Depends
from schemas.schemas import AdminUserDisplay, UserAuth, UserBase
from sqlalchemy.orm import Session
from database.database import get_db
from database_functions import db_user
from authentication import auth

router = APIRouter(
    tags=['Admin Accounts'],
    prefix='/admin/accounts',
)


@router.post('/create_user', response_model=AdminUserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db),
                admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_user.admin_create_user(request, db, admin.id)


@router.get('/get_user/{user_id}')
def admin_get_user(user_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_user.admin_get_user(user_id, db, admin.id)


@router.get('/get_all_users')
def admin_get_all_users(db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_user.admin_get_all_users(db, admin.id)


@router.get('/get_user_by_username/{username}')
def admin_get_user_by_username(username: str, db: Session = Depends(get_db),
                               admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_user.admin_get_user_by_username(username, db, admin.id)


@router.get('/get_user_by_name/{full_name}')
def admin_get_user_by_full_name(full_name: str, db: Session = Depends(get_db),
                                admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_user.admin_get_user_by_full_name(full_name, db, admin.id)


@router.get('/get_users_by_city')
def admin_get_users_by_city(city_id: int, db: Session = Depends(get_db),
                            admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_user.admin_get_user_by_city(city_id, db, admin.id)


@router.get('/get_users_by_region')
def admin_get_users_by_region(region_id: int, db: Session = Depends(get_db),
                              admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_user.admin_get_user_by_region(region_id, db, admin.id)


@router.put('/promote_user/{id}')
def promote_user_to_admin(id: int, db: Session = Depends(get_db),
                          admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_user.promotr_to_admin(user_id=id, db=db, admin_id=admin.id)


@router.delete('/delete_user')
def admin_delete_user(user_id: int, db: Session = Depends(get_db),
                      admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_user.admin_delete_user(user_id, db, admin.id)
