from fastapi import APIRouter, Depends
from schemas.schemas import CityDisplay
from sqlalchemy.orm import Session
from database.database import get_db
from database_functions import db_city
from typing import List

router = APIRouter(prefix='/city', tags=['City'])


@router.get('/city_by_id', response_model=CityDisplay)
def get_city_by_id(id: int, db: Session = Depends(get_db)):
    return db_city.get_city_by_id(id, db)


@router.get('/city_all', response_model=List[CityDisplay])
def get_all_cities(db: Session = Depends(get_db)):
    return db_city.get_all_cities(db)


@router.get('/cities_by_region', response_model=List[CityDisplay])
def get_cities_by_region(region_id: int, db: Session = Depends(get_db)):
    return db_city.get_cities_by_region(region_id, db)


@router.get('/get_cities_by_region_name/{region_name}', response_model=List[CityDisplay])
def get_cities_by_region(region_name: str, db: Session = Depends(get_db)):
    return db_city.get_cities_by_region_name(region_name, db)
