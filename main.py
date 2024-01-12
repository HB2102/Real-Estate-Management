from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database.database import Base, engine
from database import models
from authentication import authentication
from routers_general import user, region, city, asset_type, bargain_type, notice, notice_picture
from routers_admin import admin_user, admin_region, admin_city, admin_asset_type, admin_bargain_type, admin_notice

app = FastAPI()
app.include_router(user.router)
app.include_router(city.router)
app.include_router(region.router)
app.include_router(notice.router)
app.include_router(asset_type.router)
app.include_router(bargain_type.router)
app.include_router(notice_picture.router)
app.include_router(authentication.router)
app.include_router(admin_user.router)
app.include_router(admin_city.router)
app.include_router(admin_region.router)
app.include_router(admin_notice.router)
app.include_router(admin_asset_type.router)
app.include_router(admin_bargain_type.router)

Base.metadata.create_all(engine)

app.mount('/files', StaticFiles(directory='pictures'), name='files')


@app.get('/')
def home():
    message = 'Welcome to Real Estate Manager'
    return message
