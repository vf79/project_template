"""Load routers."""

from app.ext.default import default_router


def configure(app):
    """Load routers in app."""
    app.include_router(default_router.router)
