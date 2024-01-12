from fastapi import APIRouter, Depends
from schemas.schemas import BargainTypeDisplay
from sqlalchemy.orm import Session
from database.database import get_db
from database_functions import db_bargain_type
from typing import List

router = APIRouter(prefix='/bargain_type', tags=['Bargain Type'])


@router.get('/bargain_type_by_id', response_model=BargainTypeDisplay)
def get_bargain_type_by_id(id: int, db: Session = Depends(get_db)):
    return db_bargain_type.get_bargain_type(id, db)


@router.get('/bargain_type_all', response_model=List[BargainTypeDisplay])
def get_all_bargain_types(db: Session = Depends(get_db)):
    return db_bargain_type.get_all_bargain_types(db)
