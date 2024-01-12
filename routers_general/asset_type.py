from fastapi import APIRouter, Depends
from schemas.schemas import AssetTypeDisplay
from sqlalchemy.orm import Session
from database.database import get_db
from database_functions import db_asset_type
from typing import List

router = APIRouter(prefix='/asset_type', tags=['Asset Type'])


@router.get('/asset_type_by_id', response_model=AssetTypeDisplay)
def get_asset_type_by_id(id: int, db: Session = Depends(get_db)):
    return db_asset_type.get_asset_type(id, db)


@router.get('/asset_type_all', response_model=List[AssetTypeDisplay])
def get_all_asset_types(db: Session = Depends(get_db)):
    return db_asset_type.get_all_asset_types(db)
