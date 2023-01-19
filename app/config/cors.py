from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://127.0.0.1",
    "http://127.0.0.1:8080",
    "http://127.0.0.1:5500",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5500",
]


def configure(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
