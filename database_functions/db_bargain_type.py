from database.models import User, BargainType
from sqlalchemy.orm import Session
from fastapi.exceptions import HTTPException
from fastapi import status


def get_bargain_type(id: int, db: Session):
    bargain_type = db.query(BargainType).filter(BargainType.id == id).first()

    if not bargain_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Type not found !')

    return bargain_type


def get_all_bargain_types(db: Session):
    bargain_types = db.query(BargainType).all()

    if not bargain_types:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='No type found !')

    return bargain_types


def admin_add_bargain_type(name: str, db: Session, admin_id: int):
    admin = db.query(User).filter(User.id == admin_id).first()
    if admin.is_admin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    check_name = db.query(BargainType).filter(BargainType.bargain_type == name).first()
    if check_name:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                            detail="Type already exists")

    bargain_type = BargainType(
        bargain_type=name
    )

    db.add(bargain_type)
    db.commit()

    return bargain_type


def admin_delete_bargain_type(id: int, db: Session, admin_id: int):
    admin = db.query(User).filter(User.id == admin_id).first()
    if admin.is_admin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    bargain_type = db.query(BargainType).filter(BargainType.id == id).first()

    if not bargain_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Type not found')

    db.delete(bargain_type)
    db.commit()

    return 'Type deleted'



def admin_update_bargain_type(id: int, name: str, db: Session, admin_id: int):
    admin = db.query(User).filter(User.id == admin_id).first()
    if admin.is_admin == False:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    bargain_type = db.query(BargainType).filter(BargainType.id == id).first()

    if not bargain_type:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Type not found')

    bargain_type.asset_type = name
    db.commit()

    return bargain_type