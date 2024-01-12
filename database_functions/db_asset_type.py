from database.models import User, AssetType
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status


def get_asset_type(id: int, db: Session):
    asset_type = db.query(AssetType).filter(AssetType.id == id).first()

    if not asset_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Type not found !')

    return asset_type


def get_all_asset_types(db: Session):
    asset_types = db.query(AssetType).all()

    if not asset_types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No type found !')

    return asset_types


def admin_add_asset_type(name: str, db: Session, admin_id: int):
    admin = db.query(User).filter(User.id == admin_id).first()
    if admin.is_admin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    check_name = db.query(AssetType).filter(AssetType.asset_type == name).first()
    if check_name:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="Type already exists")

    asset_type = AssetType(
        asset_type=name
    )

    db.add(asset_type)
    db.commit()

    return asset_type


def admin_delete_asset_type(id: int, db: Session, admin_id: int):
    admin = db.query(User).filter(User.id == admin_id).first()
    if admin.is_admin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    asset_type = db.query(AssetType).filter(AssetType.id == id).first()

    if not asset_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Type not found')

    db.delete(asset_type)
    db.commit()

    return 'Type deleted'



def admin_update_asset_type(id: int, name: str, db: Session, admin_id: int):
    admin = db.query(User).filter(User.id == admin_id).first()
    if admin.is_admin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    asset_type = db.query(AssetType).filter(AssetType.id == id).first()

    if not asset_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Type not found')

    asset_type.asset_type = name
    db.commit()

    return asset_type