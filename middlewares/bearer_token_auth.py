from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

# BEARER_TOKEN = "?jn0TNpAdEgk!aT:)nyLx,<i=F;7D3i2L%6A2oxz[&8Cbj1U;o+lw!?6G~DKp0"
BEARER_TOKEN = "fqItdRnpqHT7nBvSAFvXBT1yTC6GJN3tOHDKINxzpNMFfkudzQjyQOVDi49wjXym"


async def bearer_token_auth(request: Request, call_next):
    try:
        headers = request.headers
        authorization = headers.get("authorization", None)
        if not authorization:
            print("No bearer token sent!")
            raise HTTPException(status_code=401, detail="No Bearer Token sent.")
        if "bearer" not in authorization.lower():
            print(
                "Bearer Token sent via incorrect format. Format should be `Bearer <token>`."
            )
            raise HTTPException(
                status_code=401,
                detail="Bearer Token sent via incorrect format. Format should be `Bearer <token>`.",
            )
        bearer_token = authorization.split()[1]
        print(bearer_token)
        if bearer_token != BEARER_TOKEN:
            print("Incorrect bearer token sent")
            raise HTTPException(status_code=403, detail="Incorrect Bearer Token sent.")
        else:
            print("Correct bearer token sent")

        response = await call_next(request)
        return response
    except HTTPException as http_exception:
        return JSONResponse(
            status_code=http_exception.status_code,
            content={"error": http_exception.detail},
        )
    except Exception as err:
        return JSONResponse(
            status_code=500, content={"error": f"Authentication failed: {err}"}
        )
