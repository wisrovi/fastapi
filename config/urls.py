from fastapi import APIRouter
from app.api.v1 import views

urls = APIRouter()

urls.include_router(
    views.router,
    prefix=""
)
