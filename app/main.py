from fastapi import FastAPI
from app.api.routes import recommendations_route, status_route

app = FastAPI(
    title="Travel Recommendations API",
    description="API for getting travel recommendations based on country and season",
    version="1.0",
    docs_url="/api/demo/docs",
    openapi_url="/api/demo/openapi.json",
    openapi_tags=[
        {
            "name": "Recommendations",
            "description": "The route to submit country and time to get a travel recommendations"
        },
        {
            "name": "Status",
            "description": "The route to get a status of process"
        }
    ],
    contact={
        "name": "Tran Vinh Liem",
        "email": "riottecboi@gmail.com",
        "url": "https://about.riotteboi.com"
    }
)

app.include_router(recommendations_route.router, prefix="/api/demo", tags=["Recommendations"])
app.include_router(status_route.router, prefix="/api/demo", tags=["Status"])