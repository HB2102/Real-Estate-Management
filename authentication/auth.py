from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, status
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from database.database import get_db
from database_functions.db_user import get_user_by_username
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

SECRET_KEY = '8f75cce3702a7e9a3469dff2ba2f4d75e908f5e965226bb230046bfdd476a862'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 3600


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta

    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    error_credential = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                     detail='invalid authorization',
                                     headers={'WWW-authenticate': 'bearer'}
                                     )

    try:
        _dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = _dict.get('sub')

        if not username:
            raise error_credential

    except JWTError:
        raise error_credential

    user = get_user_by_username(username, db)

    return user

def get_current_user_admin(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    error_credential = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                     detail='invalid authorization',
                                     headers={'WWW-authenticate': 'bearer'}
                                     )

    try:
        _dict = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username = _dict.get('sub')

        if not username:
            raise error_credential


    except JWTError:
        raise error_credential

    user = get_user_by_username(username, db)

    if user.is_admin == False:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Protected'
        )

    return user
