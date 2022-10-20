from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse
from config.settings import API_VERSION

router = APIRouter()


@router.get('/version', tags=["meta"])
def version():
    response ={
        "version":API_VERSION,
        "message" : "RPA API test 1"
    }

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response
    )