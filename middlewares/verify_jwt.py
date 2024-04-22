from typing import Annotated
from fastapi import Header, HTTPException
import jwt
from middlewares.bearer_token_auth import BEARER_TOKEN

# JWT
SECRET_KEY = BEARER_TOKEN
ALGORITHM = "HS256"


def verify_jwt(JWTAuthorization: Annotated[str, Header()]):
    print(f"Provided JWT: {JWTAuthorization}")
    try:
        decoded_jwt = jwt.decode(
            jwt=JWTAuthorization, key=SECRET_KEY, algorithms=[f"{ALGORITHM}"]
        )
        return decoded_jwt
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="JWT Expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
