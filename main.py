from fastapi import FastAPI
from database.database import Base, engine
from database import models

app = FastAPI()

Base.metadata.create_all(engine)


@app.get('/')
def home():
    message = 'Welcome to Real State Manager'
    return message
