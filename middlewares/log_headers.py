from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse


async def log_headers(request: Request, call_next):
    print("Headers:", request.headers)
    response = await call_next(request)
    return response
