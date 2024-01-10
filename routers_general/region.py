from fastapi import APIRouter, Depends
from schemas.schemas import UserDisplay, RegionDisplay, UserAuth
from sqlalchemy.orm import Session
from database.database import get_db
from database_functions import db_region
from authentication import auth
from typing import List

router = APIRouter(prefix='/region', tags=['Region'])

@router.get('/region_by_id', response_model=RegionDisplay)
def get_region_by_id(id: int, db: Session = Depends(get_db)):
    return db_region.get_region_by_id(id, db)


@router.get('/region_all', response_model=List[RegionDisplay])
def get_all_regions(db: Session = Depends(get_db)):
    return db_region.get_all_regions(db)

