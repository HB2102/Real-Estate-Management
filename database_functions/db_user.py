from database.models import User, Region, City
from schemas.schemas import UserBase
from sqlalchemy.orm import Session
from database.hash import Hash
from fastapi.exceptions import HTTPException
from fastapi import status


def create_user(request: UserBase, db: Session):
    check_username = request.username
    checked_username = check_username_duplicate(check_username, db)
    if checked_username:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail='This username already exists')

    user = User(
        username=request.username,
        password=Hash.bcrypt(request.password),
        email=request.email,
        full_name=request.full_name,
        real_estate_name=request.real_estate_name,
        phone_number=request.phone_number,
        phone=request.phone,
        region_id=request.region_id,
        city_id=request.city_id,
        street_address=request.street_address,
        is_admin=False,
    )

    db.add(user)
    db.commit()

    return show_user(user.id, db)


def show_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    region = db.query(Region).filter(Region.id == user.region_id).first()
    city = db.query(City).filter(City.id == user.city_id).first()

    if not region:
        region_name = 'Unknown'
    else:
        region_name = region.region_name

    if not city:
        city_name = 'Unknown'
    else:
        city_name = city.city_name

    display = {
        'username': user.username,
        'full_name': user.full_name,
        'email': user.email,
        'phone_number': user.phone_number,
        'real_estate_name': user.real_estate_name,
        'phone': user.phone,
        'region_name': region_name,
        'city_name': city_name,
        'street_address': user.street_address,
    }

    return display


def admin_show_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    region = db.query(Region).filter(Region.id == user.region_id).first()
    city = db.query(City).filter(City.id == user.city_id).first()

    if not region:
        region_name = 'Unknown'
    else:
        region_name = region.region_name

    if not city:
        city_name = 'Unknown'
    else:
        city_name = city.city_name

    display = {
        'id': user.id,
        'username': user.username,
        'full_name': user.full_name,
        'email': user.email,
        'phone_number': user.phone_number,
        'real_estate_name': user.real_estate_name,
        'phone': user.phone,
        'region_name': region_name,
        'city_name': city_name,
        'street_address': user.street_address,
    }

    return display


def admin_create_user(request: UserBase, db: Session, admin_id: int):
    admin = db.query(User).filter(User.id == admin_id).first()
    if admin.is_admin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    check_username = request.username
    checked_username = check_username_duplicate(check_username, db)
    if checked_username:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail='This username already exists')

    user = User(
        username=request.username,
        password=Hash.bcrypt(request.password),
        email=request.email,
        full_name=request.full_name,
        real_estate_name=request.real_estate_name,
        phone_number=request.phone_number,
        phone=request.phone,
        region_id=request.region_id,
        city_id=request.city_id,
        street_address=request.street_address,
        is_admin=False,
    )

    db.add(user)
    db.commit()

    return admin_show_user(user.id, db)


def check_username_duplicate(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    if user:
        return True
    else:
        return False


def get_user_by_username(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User not found !')

    return user
