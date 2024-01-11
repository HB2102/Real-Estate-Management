from database.models import User, Region, City, Notice
from schemas.schemas import UserBase, NoticeBase
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import and_
from database.hash import Hash
from fastapi.exceptions import HTTPException
from fastapi import status
import datetime


def create_notice(request: NoticeBase, db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    check_title = db.query(Notice).filter(
        and_(Notice.user_id == user.id, Notice.id_for_real_estate == request.id_for_real_estate)).first()
    if check_title:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="This ID already exists")

    notice = Notice(
        user_id=user.id,
        title=request.title,
        region_id=request.region_id,
        city_id=request.city_id,
        is_available=True,
        created_at=datetime.datetime.now(),
        substruction=request.substruction,
        propertyـsize=request.propertyـsize,
        number_of_floors=request.number_of_floors,
        number_of_house_units=request.number_of_house_units,
        floor=request.floor,
        room_number=request.room_number,
        area=request.area,
        neighbourhood=request.neighbourhood,
        address=request.address,
        prepayment=request.prepayment,
        price=request.price,
        description=request.description,
        asset_type_id=request.asset_type_id,
        bargain_type_id=request.bargain_type_id,
        id_for_real_estate=request.id_for_real_estate,
    )

    db.add(notice)
    db.commit()

    return notice


def show_notice(notice_id: int, db: Session):
    notice = db.query(Notice).filter(Notice.id == notice_id).first()
    if not notice:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    user = db.query(User).filter(User.id == notice.user_id).first()

    region = db.query(Region).filter(Region.id == user.region_id).first()
    if not region:
        region_name = 'Unknown'
    else:
        region_name = region.region_name

    city = db.query(City).filter(City.id == user.city_id).first()
    if not city:
        city_name = "Unknown"
    else:
        city_name = city.city_name

    user_display = {
        'full_name': user.full_name,
        'phone_number': user.phone_number,
        'real_estate_name': user.real_estate_name,
        'phone': user.phone,
        'region': region_name,
        'city': city_name,
        'street_address': user.street_address
    }

    display = {
        'user': user_display,
        'title': notice.title,
        'region_id': notice.region_id,
        'city_id': notice.city_id,
        'substruction': notice.substruction,
        'propertyـsize': notice.propertyـsize,
        'number_of_floors': notice.number_of_floors,
        'number_of_house_units': notice.number_of_house_units,
        'floor': notice.floor,
        'room_number': notice.room_number,
        'area': notice.area,
        'neighbourhood': notice.neighbourhood,
        'address': notice.address,
        'prepayment': notice.prepayment,
        'price': notice.price,
        'description': notice.description,
        'asset_type_id': notice.asset_type_id,
        'bargain_type_id': notice.bargain_type_id,
    }

    return display


def real_estate_show_notice(notice_id: int, db: Session):
    notice = db.query(Notice).filter(Notice.id == notice_id).first()
    if not notice:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    user = db.query(User).filter(User.id == notice.user_id).first()

    region = db.query(Region).filter(Region.id == user.region_id).first()
    if not region:
        region_name = 'Unknown'
    else:
        region_name = region.region_name

    city = db.query(City).filter(City.id == user.city_id).first()
    if not city:
        city_name = "Unknown"
    else:
        city_name = city.city_name

    user_display = {
        'username': user.username,
        'full_name': user.full_name,
        'phone_number': user.phone_number,
        'real_estate_name': user.real_estate_name,
        'phone': user.phone,
        'region': region_name,
        'city': city_name,
        'street_address': user.street_address
    }

    display = {
        'user': user_display,
        'title': notice.title,
        'region_id': notice.region_id,
        'city_id': notice.city_id,
        'substruction': notice.substruction,
        'propertyـsize': notice.propertyـsize,
        'number_of_floors': notice.number_of_floors,
        'number_of_house_units': notice.number_of_house_units,
        'floor': notice.floor,
        'room_number': notice.room_number,
        'area': notice.area,
        'neighbourhood': notice.neighbourhood,
        'address': notice.address,
        'prepayment': notice.prepayment,
        'price': notice.price,
        'description': notice.description,
        'asset_type_id': notice.asset_type_id,
        'bargain_type_id': notice.bargain_type_id,
        'is_available': notice.is_available,
    }

    return display


def admin_show_notice(notice_id: int, db: Session):
    notice = db.query(Notice).filter(Notice.id == notice_id).first()
    if not notice:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    user = db.query(User).filter(User.id == notice.user_id).first()

    region = db.query(Region).filter(Region.id == user.region_id).first()
    if not region:
        region_name = 'Unknown'
    else:
        region_name = region.region_name

    city = db.query(City).filter(City.id == user.city_id).first()
    if not city:
        city_name = "Unknown"
    else:
        city_name = city.city_name

    user_display = {
        'id': user.id,
        'username': user.username,
        'full_name': user.full_name,
        'phone_number': user.phone_number,
        'real_estate_name': user.real_estate_name,
        'phone': user.phone,
        'region': region_name,
        'city': city_name,
        'street_address': user.street_address
    }

    display = {
        'user': user_display,
        'id': notice.id,
        'title': notice.title,
        'region_id': notice.region_id,
        'city_id': notice.city_id,
        'substruction': notice.substruction,
        'propertyـsize': notice.propertyـsize,
        'number_of_floors': notice.number_of_floors,
        'number_of_house_units': notice.number_of_house_units,
        'floor': notice.floor,
        'room_number': notice.room_number,
        'area': notice.area,
        'neighbourhood': notice.neighbourhood,
        'address': notice.address,
        'prepayment': notice.prepayment,
        'price': notice.price,
        'description': notice.description,
        'asset_type_id': notice.asset_type_id,
        'bargain_type_id': notice.bargain_type_id,
        'is_available': notice.is_available,
    }

    return display


def get_notice(notice_id: int, db: Session):
    notice = db.query(Notice).filter(Notice.id == notice_id).first()
    if notice.is_available == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Notice is not available anymore')

    return show_notice(notice.id, db)


def get_self_notice(notice_id: int, db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    notice = db.query(Notice).filter(Notice.id == notice_id).first()

    if notice.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Not Authorized')

    if notice.is_available == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Notice is not available anymore')

    return real_estate_show_notice(notice.id, db)


def admin_get_notice(notice_id: int, db: Session, admin_id: int):
    admin = db.query(User).filter(User.id == admin_id).first()
    if admin.is_admin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return admin_show_notice(notice_id, db)


def user_get_all_self_notice(db: Session, user_id: int):
    notices = db.query(Notice).filter(Notice.user_id == user_id).all()
    if not notices:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    display = []
    for notice in notices:
        display.append(real_estate_show_notice(notice.id, db))

    return display


def user_get_all_self_available_notice(db: Session, user_id: int):
    notices = db.query(Notice).filter(Notice.user_id == user_id).all()
    if not notices:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    display = []
    for notice in notices:
        if notice.is_available == True:
            display.append(real_estate_show_notice(notice.id, db))

    if not display:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No notice was found')

    return display


# ============================================================================================================
# ============================================================================================================
# ============================================================================================================
# ============================================================================================================


def get_all_notices(db: Session):
    notices = db.query(Notice).all()
    if not notices:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    display = []
    for notice in notices:
        if notice.is_available == True:
            display.append(show_notice(notice.id, db))

    if not display:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No notice was found')

    return display


def get_all_notices_by_region(region_id: int, db: Session):
    notices = db.query(Notice).filter(Notice.region_id == region_id).all()
    if not notices:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    display = []
    for notice in notices:
        if notice.is_available == True:
            display.append(show_notice(notice.id, db))

    if not display:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No notice was found')

    return display


def get_all_notices_by_city(city_id: int, db: Session):
    notices = db.query(Notice).filter(Notice.city_id == city_id).all()
    if not notices:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    display = []
    for notice in notices:
        if notice.is_available == True:
            display.append(show_notice(notice.id, db))

    if not display:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No notice was found')

    return display


def get_all_notices_by_asset_type(asset_type_id: int, db: Session):
    notices = db.query(Notice).filter(Notice.asset_type_id == asset_type_id).all()
    if not notices:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    display = []
    for notice in notices:
        if notice.is_available == True:
            display.append(show_notice(notice.id, db))

    if not display:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No notice was found')

    return display


def get_all_notices_by_bargain_type(bargain_type_id: int, db: Session):
    notices = db.query(Notice).filter(Notice.bargain_type_id == bargain_type_id).all()
    if not notices:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    display = []
    for notice in notices:
        if notice.is_available == True:
            display.append(show_notice(notice.id, db))

    if not display:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No notice was found')

    return display


# ============================================================================================================
# ============================================================================================================
# ============================================================================================================
# ============================================================================================================

def get_all_notices_by_region_bargain_type(region_id: int, bargain_type_id: int, db: Session):
    notices = db.query(Notice).filter(and_(Notice.region_id == region_id, Notice.bargain_type_id == bargain_type_id)).all()
    if not notices:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    display = []
    for notice in notices:
        if notice.is_available == True:
            display.append(show_notice(notice.id, db))

    if not display:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No notice was found')

    return display


def get_all_notices_by_city_bargain_type(city_id: int, bargain_type_id: int, db: Session):
    notices = db.query(Notice).filter(and_(Notice.city_id == city_id, Notice.bargain_type_id == bargain_type_id)).all()
    if not notices:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    display = []
    for notice in notices:
        if notice.is_available == True:
            display.append(show_notice(notice.id, db))

    if not display:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No notice was found')

    return display


def get_all_notices_by_region_asset_type(region_id: int, asset_type_id: int, db: Session):
    notices = db.query(Notice).filter(and_(Notice.region_id == region_id, Notice.asset_type_id == asset_type_id)).all()
    if not notices:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    display = []
    for notice in notices:
        if notice.is_available == True:
            display.append(show_notice(notice.id, db))

    if not display:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No notice was found')

    return display


def get_all_notices_by_city_asset_type(city_id: int, asset_type_id: int, db: Session):
    notices = db.query(Notice).filter(and_(Notice.city_id == city_id, Notice.asset_type_id == asset_type_id)).all()
    if not notices:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    display = []
    for notice in notices:
        if notice.is_available == True:
            display.append(show_notice(notice.id, db))

    if not display:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No notice was found')

    return display


def get_all_notices_by_bargain_type_asset_type(bargain_type_id: int, asset_type_id: int, db: Session):
    notices = db.query(Notice).filter(and_(Notice.bargain_type_id == bargain_type_id, Notice.asset_type_id == asset_type_id)).all()
    if not notices:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    display = []
    for notice in notices:
        if notice.is_available == True:
            display.append(show_notice(notice.id, db))

    if not display:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No notice was found')

    return display


# ============================================================================================================
# ============================================================================================================
# ============================================================================================================
# ============================================================================================================

def get_all_notices_by_region_bargain_type_asset_type(region_id: int, bargain_type_id: int, asset_type_id: int, db: Session):
    notices = db.query(Notice).filter(and_(Notice.region_id == region_id, Notice.bargain_type_id == bargain_type_id, Notice.asset_type_id == asset_type_id)).all()
    if not notices:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    display = []
    for notice in notices:
        if notice.is_available == True:
            display.append(show_notice(notice.id, db))

    if not display:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No notice was found')

    return display

def get_all_notices_by_city_bargain_type_asset_type(city_id: int, bargain_type_id: int, asset_type_id: int, db: Session):
    notices = db.query(Notice).filter(and_(Notice.city_id == city_id, Notice.bargain_type_id == bargain_type_id, Notice.asset_type_id == asset_type_id)).all()
    if not notices:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    display = []
    for notice in notices:
        if notice.is_available == True:
            display.append(show_notice(notice.id, db))

    if not display:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No notice was found')

    return display


# ============================================================================================================
# ============================================================================================================
# ============================================================================================================
# ============================================================================================================


def get_notice_info(notice_id: int, db: Session):
    notice = db.query(Notice).filter(Notice.id == notice_id).first()
    if not notice:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found')

    user = db.query(User).filter(User.id == notice.user_id).first()

    region = db.query(Region).filter(Region.id == user.region_id).first()
    if not region:
        region_name = 'Unknown'
    else:
        region_name = region.region_name

    city = db.query(City).filter(City.id == user.city_id).first()
    if not city:
        city_name = "Unknown"
    else:
        city_name = city.city_name

    user_display = {
        'full_name': user.full_name,
        'phone_number': user.phone_number,
        'real_estate_name': user.real_estate_name,
        'phone': user.phone,
        'region': region_name,
        'city': city_name,
        'street_address': user.street_address,
    }

    return user_display
