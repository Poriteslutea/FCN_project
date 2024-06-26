from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import create_db_and_tables
from routers import member, report, product


app = FastAPI()

# 這個可依models.py所設的建立table
@app.on_event("startup")
def on_startup():
   create_db_and_tables()


subapi = FastAPI()

subapi.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

subapi.include_router(member.router)
subapi.include_router(report.router)
subapi.include_router(product.router)

@subapi.get('/')
def hw():
    print('hi')
    return 'Hello world!'


app.mount("/api", subapi)