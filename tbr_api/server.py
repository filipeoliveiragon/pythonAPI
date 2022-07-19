from fastapi import FastAPI
from tbr_api.routers import user_router, atividade_router

app = FastAPI()

app.include_router(user_router.router)
app.include_router(atividade_router.router)