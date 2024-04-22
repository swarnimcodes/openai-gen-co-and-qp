from openai import OpenAI

from fastapi import APIRouter
from fastapi.responses import JSONResponse


client = OpenAI()
router = APIRouter()


@router.get("/verify_openai_api_key")
async def verify_openai_api_key():
    try:
        # print(f"{client.api_key}") # check if API Key is being read properly by printing this
        _ = client.models.list()
        return JSONResponse(
            status_code=200, content={"message": "OpenAI API Key Verified"}
        )
    except Exception as err:
        return JSONResponse(
            status_code=500,
            content={"error": f"Failed to verify OpenAI API Key: {err}"},
        )
