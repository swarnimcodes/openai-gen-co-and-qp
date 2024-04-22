import time
import json
from fastapi import Body, APIRouter
from fastapi.responses import JSONResponse
import jwt
from typing import Dict, Any
from middlewares.bearer_token_auth import BEARER_TOKEN

SECRET_KEY = BEARER_TOKEN
ALGORITHM = "HS256"

router = APIRouter()


@router.get("/create_jwt")
async def create_jwt(data: Dict[str, Any] = Body(...)):
    print(json.dumps(data, indent=2))
    seconds_to_expiry = 60 * 30
    curtime = time.time()
    iat = int(curtime)
    exp = iat + seconds_to_expiry
    data["exp"] = exp
    data["iat"] = iat

    token = jwt.encode(payload=data, key=SECRET_KEY, algorithm=ALGORITHM)
    return JSONResponse(
        status_code=200,
        content={"jwt": token, "encoded_data": data},
    )
