import os, sys
path = os.environ['FILE_PATH']
sys.path.append(path)

from app.api_v1.routes import api_router
from fastapi import APIRouter, FastAPI


app = FastAPI(title="", openapi_url="")
app.include_router(api_router, prefix="", tags=[""])
