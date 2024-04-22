from fastapi import FastAPI, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from typing import Dict, Any

# Custom Middleware
from middlewares.bearer_token_auth import bearer_token_auth, BEARER_TOKEN
from middlewares.log_headers import log_headers
from middlewares.verify_jwt import verify_jwt

# Routes
from routes.jwt.create_jwt import router as create_jwt_router
from routes.openai.verify_openai_api_key import router as verify_openai_api_key_router
from routes.openai.list_available_models import router as list_available_models_router
from routes.openai.generate_course_outcomes import (
    router as generate_course_outcomes_router,
)
from routes.openai.generate_question_paper import (
    router as generate_question_paper_router,
)
from routes.openai.get_openai_api_key import router as get_openai_api_key_router


app = FastAPI()

# JWT
SECRET_KEY = BEARER_TOKEN
ALGORITHM = "HS256"

# Register Middlewares
# - CORS Middleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)
# - Bearer Token Authorization Middleware
app.middleware("http")(bearer_token_auth)
app.middleware("http")(log_headers)

# Attach Routes to the main app
app.include_router(create_jwt_router)
app.include_router(verify_openai_api_key_router)
app.include_router(generate_course_outcomes_router)
app.include_router(list_available_models_router)
app.include_router(generate_question_paper_router)
app.include_router(get_openai_api_key_router)


@app.get("/", dependencies=[Depends(verify_jwt)])
async def hello(decoded_jwt: Dict[str, Any] = Depends(verify_jwt)):
    return JSONResponse(
        status_code=200,
        content={"message": "hello from msaigco!", "decoded_jwt": decoded_jwt},
    )
