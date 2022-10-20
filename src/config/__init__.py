import os
from fastapi import FastAPI
from fastapi.middleware.cors import  CORSMiddleware

from config import urls
from config.settings import API_VERSION

app = FastAPI(
    title="RPA API",
    description="RPA API",
    version=API_VERSION,
    redoc_url="/api/v1/docs",
    docs_url="/api/v1/docs"
)

origins =["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(
    urls.urls
)