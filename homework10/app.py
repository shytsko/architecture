from fastapi import FastAPI
from routes.client_routes import client_router
from routes.pet_routes import pet_router
from routes.consultation_route import consultation_router

app = FastAPI(title="Clinic Service")

app.include_router(client_router)
app.include_router(pet_router)
app.include_router(consultation_router)
