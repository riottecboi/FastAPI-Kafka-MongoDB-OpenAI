from fastapi import FastAPI
from app.api.routes import recommendations_route

app = FastAPI()

app.include_router(recommendations_route.router)