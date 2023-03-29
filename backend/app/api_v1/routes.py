import os, sys
path = os.environ['FILE_PATH']
sys.path.append(path)

from fastapi import APIRouter
from app.api_v1.controller.JsonToPdfController import jsonToPdfService

api_router = APIRouter()
api_router.include_router(jsonToPdfService, prefix="/api/v1/json-to-pdf", tags=["json-to-pdf"])

