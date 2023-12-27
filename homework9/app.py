from fastapi import FastAPI
from routes.weather_forecast_route import weather_forecast_router

app = FastAPI(title="Weather Forecast Service")

app.include_router(weather_forecast_router)
