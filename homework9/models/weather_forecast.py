from pydantic import BaseModel
from datetime import date


class WeatherForecastBase(BaseModel):
    temperature_c: int
    date: date


class WeatherForecastIn(WeatherForecastBase):
    pass


class WeatherForecastOut(WeatherForecastBase):
    temperature_f: int
