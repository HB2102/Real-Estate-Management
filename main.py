from fastapi import FastAPI



app = FastAPI()



@app.get('/')
def home():
    message = 'Welcome to Real State Manager'
    return message