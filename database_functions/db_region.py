from database.models import User, Region, City
from schemas.schemas import UserBase
from sqlalchemy.orm import Session
from database.hash import Hash
from fastapi.exceptions import HTTPException
from fastapi import status


def get_region_by_id(id: int, db: Session):
    region = db.query(Region).filter(Region.id == id).first()

    if not region:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Region not found !')

    return region


def get_all_regions(db: Session):
    regions = db.query(Region).all()

    if not regions:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No region found !')

    return regions


def admin_add_region(name: str, db: Session, admin_id: int):
    admin = db.query(User).filter(User.id == admin_id).first()
    if admin.is_admin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    check_name = db.query(Region).filter(Region.region_name == name).first()
    if check_name:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="Region already exists")

    region = Region(
        region_name=name
    )

    db.add(region)
    db.commit()

    return region


def admin_delete_region(id: int, db: Session, admin_id: int):
    admin = db.query(User).filter(User.id == admin_id).first()
    if admin.is_admin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    region = db.query(Region).filter(Region.id == id).first()

    if not region:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Region not found')

    db.delete(region)
    db.commit()

    return 'Region deleted'


def admin_update_region(id: int, name: str, db: Session, admin_id: int):
    admin = db.query(User).filter(User.id == admin_id).first()
    if admin.is_admin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    region = db.query(Region).filter(Region.id == id).first()

    if not region:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Region not found')

    region.region_name = name
    db.commit()

    return region
