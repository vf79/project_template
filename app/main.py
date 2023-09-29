"""Project Template main."""
from fastapi import FastAPI

from app.config import cors, routers


def create_app():
    """Create app fastapi framework."""
    app = FastAPI()
    cors.configure(app)
    routers.configure(app)
    return app


app = create_app()
