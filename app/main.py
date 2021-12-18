from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models
from .database import engine

from .routers import post, qna, users, auth

models.Base.metadata.create_all(bind=engine)
app = FastAPI()





while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fast_api', user='postgres', password='Python123',cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('working')
        break
    except Exception as error:
        print('database not connected')
        print(error)
        time.sleep(3)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(qna.router)



