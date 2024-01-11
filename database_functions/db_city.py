from database.models import User, Region, City
from schemas.schemas import UserBase
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import and_
from database.hash import Hash
from fastapi.exceptions import HTTPException
from fastapi import status


def get_city_by_id(id: int, db: Session):
    city = db.query(City).filter(City.id == id).first()

    if not city:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='City not found !')

    return city


def get_all_cities(db: Session):
    cities = db.query(City).all()

    if not cities:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No city found !')

    return cities


def get_cities_by_region(region_id: int, db: Session):
    cities = db.query(City).filter(City.region_id == region_id).all()

    if not cities:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No city found !')

    return cities



def get_cities_by_region_name(region_name: str, db: Session):
    region = db.query(Region).filter(Region.region_name == region_name).first()
    if not region:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Region not found')
    cities = db.query(City).filter(City.region_id == region.id).all()

    if not cities:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No city found !')

    return cities


def admin_add_city(name: str, region_id: int, db: Session, admin_id: int):
    admin = db.query(User).filter(User.id == admin_id).first()
    if admin.is_admin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    check_name = db.query(City).filter(and_(City.city_name == name, City.region_id == region_id)).first()
    if check_name:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="City already exists")

    city = City(
        city_name=name,
        region_id=region_id
    )

    db.add(city)
    db.commit()

    return city


def admin_delete_city(id: int, db: Session, admin_id: int):
    admin = db.query(User).filter(User.id == admin_id).first()
    if admin.is_admin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    city = db.query(City).filter(City.id == id).first()

    if not city:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='City not found')

    db.delete(city)
    db.commit()

    return 'City deleted'



def admin_update_city(id: int, name: str, db: Session, admin_id: int):
    admin = db.query(User).filter(User.id == admin_id).first()
    if admin.is_admin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    city = db.query(City).filter(City.id == id).first()

    if not city:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='City not found')

    city.city_name = name
    db.commit()

    return city
