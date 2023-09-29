"""Default router."""
from fastapi import APIRouter

from app.config import config

router = APIRouter()
settings = config.get_settings()


@router.get("/", tags=["Home"])
async def home():
    """Return Default Home Page."""
    data = {
        "name": settings.name,
        "version": settings.version,
        "ambiente": settings.ambiente,
    }
    return data
