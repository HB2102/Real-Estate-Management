from fastapi import FastAPI
from database.database import Base, engine
from database import models
from authentication import authentication
from routers_general import user, region, city, asset_type
from routers_admin import admin_user, admin_region, admin_city, admin_asset_type



app = FastAPI()
app.include_router(user.router)
app.include_router(region.router)
app.include_router(city.router)
app.include_router(asset_type.router)
app.include_router(authentication.router)
app.include_router(admin_user.router)
app.include_router(admin_region.router)
app.include_router(admin_city.router)
app.include_router(admin_asset_type.router)

Base.metadata.create_all(engine)


@app.get('/')
def home():
    message = 'Welcome to Real Estate Manager'
    return message
