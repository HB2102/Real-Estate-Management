from database.models import User
from schemas.schemas import UserBase, UpdateUserBase
from sqlalchemy.orm import Session
from database.hash import Hash
from fastapi.exceptions import HTTPException
from fastapi import status





def get_user_by_username(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='User not found !')

    return user