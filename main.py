from fastapi import FastAPI
from database.database import Base, engine
from database import models
from authentication import authentication
from routers_general import user, region
from routers_admin import admin_user



app = FastAPI()
app.include_router(user.router)
app.include_router(region.router)
app.include_router(authentication.router)
app.include_router(admin_user.router)

Base.metadata.create_all(engine)


@app.get('/')
def home():
    message = 'Welcome to Real Estate Manager'
    return message
