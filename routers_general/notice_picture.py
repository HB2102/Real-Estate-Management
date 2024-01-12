from fastapi import APIRouter, Depends, status, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.exceptions import HTTPException
from schemas.schemas import UserAuth
from sqlalchemy.orm import Session
from database.database import get_db
from database.models import NoticePicture, User, Notice
from authentication import auth
from string import ascii_letters
import os
import random
import shutil

router = APIRouter(
    tags=['Picture'],
    prefix='/file',
)


@router.post('/upload_notice_image/{notice_id}')
def upload_book_picture(notice_id: int, file: UploadFile = File(...), db: Session = Depends(get_db), user: UserAuth = Depends(auth.get_current_user)):
    user = db.query(User).filter(User.id == user.id).first()
    notice = db.query(Notice).filter(Notice.id == notice_id).first()

    if not notice:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail='Notice not found !')

    if notice.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Not Authorized')

    rand_str = ''.join(random.choice(ascii_letters) for _ in range(6))
    new_name = f'_{rand_str}.'.join(file.filename.rsplit('.', 1))


    path_file = f'pictures/{new_name}'

    notice_picture = NoticePicture(
        notice_id=notice_id,
        picture_path=path_file,
    )

    db.add(notice_picture)
    db.commit()

    with open(path_file, 'w+b') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return 'Picture Uploaded'


@router.delete('/delete_picture_of_notice')
def delete_notice_picture(notice_id: int, db: Session = Depends(get_db), user: UserAuth = Depends(auth.get_current_user)):
    user = db.query(User).filter(User.id == user.id).first()
    notice = db.query(Notice).filter(Notice.id == notice_id).first()

    if notice.user_id != user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Not Authorized')

    pictures = db.query(NoticePicture).filter(NoticePicture.notice_id == notice_id).all()

    if not pictures:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No picture found !')

    for picture in pictures:
        if os.path.exists(picture.picture_path):
            os.remove(picture.picture_path)

        db.delete(picture)
        db.commit()

    return 'All pictures deleted.'


@router.get('/get_one_picture_of_notice/{notice_id}', response_class=FileResponse)
def get_one_picture_of_notice(notice_id: int, db: Session = Depends(get_db)):
    notice = db.query(Notice).filter(Notice.id == notice_id).first()
    if not notice:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notice not found !")

    picture = db.query(NoticePicture).filter(NoticePicture.notice_id == notice_id).first()
    if not picture:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No picture found !")

    pic = picture.picture_path

    return pic


@router.get('/get_url_pictures_of_notice/{notice_id}')
def get_pictures_of_notice(notice_id: int, db: Session = Depends(get_db)):
    notice = db.query(Notice).filter(Notice.id == notice_id).first()
    if not notice:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Notice not found !")

    pictures = db.query(NoticePicture).filter(NoticePicture.notice_id == notice_id).all()
    if not pictures:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No picture found !")

    display = []
    for picture in pictures:
        display.append(picture.picture_path)

    return display


