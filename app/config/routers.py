from app.ext.default import default_router


def configure(app):
    app.include_router(default_router.router)
