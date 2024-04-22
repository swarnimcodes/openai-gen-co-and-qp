from openai import OpenAI

from fastapi import APIRouter
from fastapi.responses import JSONResponse
import json


client = OpenAI()
router = APIRouter()


@router.get("/v1/list_available_models")
async def list_available_models():
    try:
        # print(f"{client.api_key}") # check if API Key is being read properly by printing this
        models = client.models.list().model_dump(mode="json")
        # print(models)
        return JSONResponse(status_code=200, content=models)
    except Exception as err:
        return JSONResponse(
            status_code=500,
            content={"error": err},
        )
