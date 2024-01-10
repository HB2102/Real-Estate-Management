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
