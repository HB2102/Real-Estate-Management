from fastapi import APIRouter, Depends
from schemas.schemas import UserAuth
from sqlalchemy.orm import Session
from database.database import get_db
from database_functions import db_notice
from authentication import auth

router = APIRouter(
    tags=['Admin Notice'],
    prefix='/admin/notice',
)


@router.get('/admin_get_notice/{id}')
def admin_get_notice(id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_notice.admin_get_notice(id, db, admin.id)


@router.get('/get_notice_user')
def admin_get_notice_user(notice_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_notice.admin_get_notice_user(notice_id, db, admin.id)


@router.get('/get_all_notices')
def admin_get_all_notices(db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_notice.admin_get_all_notices(db, admin.id)


@router.get('/get_all_notices_by_region')
def admin_get_all_notices_by_region(region_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_notice.admin_get_all_notices_by_region(region_id, db, admin.id)


@router.get('/get_all_notices_by_city')
def admin_get_all_notices_by_region(city_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_notice.admin_get_all_notices_by_city(city_id, db, admin.id)


@router.get('/get_all_notices_by_asset_type')
def admin_get_all_notices_by_asset_type(asset_type_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_notice.admin_get_all_notices_by_asset_type(asset_type_id, db, admin.id)


@router.get('/get_all_notices_by_bargain_type')
def admin_get_all_notices_by_bargain_type(bargain_type_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_notice.admin_get_all_notices_by_bargain_type(bargain_type_id, db, admin.id)


# ============================================================================================================
# ============================================================================================================
# ============================================================================================================
# ============================================================================================================

@router.get('/get_all_notices_by_region_bargain_type')
def admin_get_all_notices_by_region_bargain_type(region_id: int, bargain_type_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_notice.admin_get_all_notices_by_region_bargain_type(region_id, bargain_type_id, db, admin.id)


@router.get('/get_all_notices_by_city_bargain_type')
def admin_get_all_notices_by_city_bargain_type(city_id: int, bargain_type_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_notice.admin_get_all_notices_by_city_bargain_type(city_id, bargain_type_id, db, admin.id)


@router.get('/get_all_notices_by_region_asset_type')
def admin_get_all_notices_by_region_asset_type(region_id: int, asset_type_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_notice.admin_get_all_notices_by_region_asset_type(region_id, asset_type_id, db, admin.id)


@router.get('/get_all_notices_by_city_asset_type')
def admin_get_all_notices_by_city_asset_type(city_id: int, asset_type_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_notice.admin_get_all_notices_by_city_asset_type(city_id, asset_type_id, db, admin.id)


@router.get('/get_all_notices_by_bargain_type_asset_type')
def admin_get_all_notices_by_bargain_type_asset_type(bargain_type_id: int, asset_type_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_notice.admin_get_all_notices_by_bargain_type_asset_type(bargain_type_id, asset_type_id, db, admin.id)

# ============================================================================================================
# ============================================================================================================
# ============================================================================================================
# ============================================================================================================


@router.get('/get_all_notices_by_region_bargain_type_asset_type')
def admin_get_all_notices_by_region_bargain_type_asset_type(region_id: int, bargain_type_id: int, asset_type_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_notice.admin_get_all_notices_by_region_bargain_type_asset_type(region_id, bargain_type_id, asset_type_id, db, admin.id)


@router.get('/get_all_notices_by_city_bargain_type_asset_type')
def adimn_get_all_notices_by_city_bargain_type_asset_type(city_id: int, bargain_type_id: int, asset_type_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_notice.admin_get_all_notices_by_city_bargain_type_asset_type(city_id, bargain_type_id, asset_type_id, db, admin.id)




@router.delete('/delete_notice')
def admin_delete_notice(notice_id: int, db: Session = Depends(get_db), admin: UserAuth = Depends(auth.get_current_user_admin)):
    return db_notice.admin_delete_notice(notice_id, db, admin.id)
