from openai import OpenAI

from fastapi import APIRouter
from fastapi.responses import JSONResponse


client = OpenAI()
router = APIRouter()


@router.get("/v1/get_openai_api_key")
async def get_openai_api_key():
    try:
        openai_api_key = client.api_key
        content = {"openai_api_key": openai_api_key}
        return JSONResponse(status_code=200, content=content)
    except Exception as err:
        return JSONResponse(
            status_code=500,
            content={"error": err},
        )
