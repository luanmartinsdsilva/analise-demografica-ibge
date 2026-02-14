from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.pessoas import router as pessoas_router

app = FastAPI(title="API de Pessoas", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pessoas_router)
