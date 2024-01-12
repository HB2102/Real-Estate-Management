from fastapi import APIRouter, Depends
from schemas.schemas import UserAuth, NoticeBase
from sqlalchemy.orm import Session
from database.database import get_db
from database_functions import db_notice
from authentication import auth

router = APIRouter(prefix='/notice', tags=['Notice'])


@router.post('/create_notice')
def create_notice(request: NoticeBase, db: Session = Depends(get_db), user: UserAuth = Depends(auth.get_current_user)):
    return db_notice.create_notice(request, db, user.id)


@router.get('/get_notice/{notice_id}')
def get_notice(notice_id, db: Session = Depends(get_db)):
    return db_notice.get_notice(notice_id, db)


@router.get('/get_self_notice/{id}')
def get_self_notice(notice_id, db: Session = Depends(get_db), user: UserAuth = Depends(auth.get_current_user)):
    return db_notice.get_self_notice(notice_id, db, user.id)


@router.get('/get_all_self_notice')
def get_all_self_notice(db: Session = Depends(get_db), user: UserAuth = Depends(auth.get_current_user)):
    return db_notice.user_get_all_self_notice(db, user.id)


@router.get('/get_all_available_self_notice')
def get_all_self_available_notice(db: Session = Depends(get_db), user: UserAuth = Depends(auth.get_current_user)):
    return db_notice.user_get_all_self_available_notice(db, user.id)


@router.get('/get_all_notices')
def get_all_notices(db: Session = Depends(get_db)):
    return db_notice.get_all_notices(db)


@router.get('/get_all_notices_by_region')
def get_all_notices_by_region(region_id: int, db: Session = Depends(get_db)):
    return db_notice.get_all_notices_by_region(region_id, db)


@router.get('/get_all_notices_by_city')
def get_all_notices_by_region(city_id: int, db: Session = Depends(get_db)):
    return db_notice.get_all_notices_by_city(city_id, db)


@router.get('/get_all_notices_by_asset_type')
def get_all_notices_by_asset_type(asset_type_id: int, db: Session = Depends(get_db)):
    return db_notice.get_all_notices_by_asset_type(asset_type_id, db)


@router.get('/get_all_notices_by_bargain_type')
def get_all_notices_by_bargain_type(bargain_type_id: int, db: Session = Depends(get_db)):
    return db_notice.get_all_notices_by_bargain_type(bargain_type_id, db)


# ============================================================================================================
# ============================================================================================================
# ============================================================================================================
# ============================================================================================================

@router.get('/get_all_notices_by_region_bargain_type')
def get_all_notices_by_region_bargain_type(region_id: int, bargain_type_id: int, db: Session = Depends(get_db)):
    return db_notice.get_all_notices_by_region_bargain_type(region_id, bargain_type_id, db)


@router.get('/get_all_notices_by_city_bargain_type')
def get_all_notices_by_city_bargain_type(city_id: int, bargain_type_id: int, db: Session = Depends(get_db)):
    return db_notice.get_all_notices_by_city_bargain_type(city_id, bargain_type_id, db)


@router.get('/get_all_notices_by_region_asset_type')
def get_all_notices_by_region_asset_type(region_id: int, asset_type_id: int, db: Session = Depends(get_db)):
    return db_notice.get_all_notices_by_region_asset_type(region_id, asset_type_id, db)


@router.get('/get_all_notices_by_city_asset_type')
def get_all_notices_by_city_asset_type(city_id: int, asset_type_id: int, db: Session = Depends(get_db)):
    return db_notice.get_all_notices_by_city_asset_type(city_id, asset_type_id, db)


@router.get('/get_all_notices_by_bargain_type_asset_type')
def get_all_notices_by_bargain_type_asset_type(bargain_type_id: int, asset_type_id: int, db: Session = Depends(get_db)):
    return db_notice.get_all_notices_by_bargain_type_asset_type(bargain_type_id, asset_type_id, db)

# ============================================================================================================
# ============================================================================================================
# ============================================================================================================
# ============================================================================================================


@router.get('/get_all_notices_by_region_bargain_type_asset_type')
def get_all_notices_by_region_bargain_type_asset_type(region_id: int, bargain_type_id: int, asset_type_id: int, db: Session = Depends(get_db)):
    return db_notice.get_all_notices_by_region_bargain_type_asset_type(region_id, bargain_type_id, asset_type_id, db)


@router.get('/get_all_notices_by_city_bargain_type_asset_type')
def get_all_notices_by_city_bargain_type_asset_type(city_id: int, bargain_type_id: int, asset_type_id: int, db: Session = Depends(get_db)):
    return db_notice.get_all_notices_by_city_bargain_type_asset_type(city_id, bargain_type_id, asset_type_id, db)

# ============================================================================================================
# ============================================================================================================
# ============================================================================================================
# ============================================================================================================


@router.get('/get_notice_info')
def get_notice_info(notice_id: int, db: Session = Depends(get_db)):
    return db_notice.get_notice_info(notice_id, db)


@router.get('/get_notice_by_id_for_real_estate/{id}')
def real_estate_get_notice_by_id_for_real_estate(id_for_real_estate: int, db: Session = Depends(get_db), user: UserAuth = Depends(auth.get_current_user)):
    return db_notice.real_estate_get_notice_by_id_for_real_estate(id_for_real_estate, db, user.id)



@router.put('/update_notice_info')
def real_estate_update_notice_info(notice_id: int, request: NoticeBase, db: Session = Depends(get_db), user: UserAuth = Depends(auth.get_current_user)):
    return db_notice.user_update_notice(notice_id, request, db, user.id)


@router.put('/make_unavailable/{id}')
def make_notice_unavailable(notice_id: int, db: Session = Depends(get_db), user: UserAuth = Depends(auth.get_current_user)):
    return db_notice.make_notice_unavailable(notice_id, db, user.id)


@router.delete('/delete_notice')
def real_estate_delete_notice(notice_id: int, db: Session = Depends(get_db), user: UserAuth = Depends(auth.get_current_user)):
    return db_notice.user_delete_notice(notice_id, db, user.id)

