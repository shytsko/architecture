from fastapi import APIRouter, HTTPException, status, Depends
from models.weather_forecast import WeatherForecastIn, WeatherForecastOut
from datetime import date as Date, datetime, timedelta
from database.weather_forecast_holder import WeatherForecastHolder, WeatherForecastDBModel

database = WeatherForecastHolder()

weather_forecast_router = APIRouter(prefix='/weather-forecast', tags=['Weather Forecast'])


@weather_forecast_router.get('/get', response_model=WeatherForecastOut)
def get(date: Date, db: WeatherForecastHolder = Depends(database)):
    weather_forecast = db.get(date)
    if weather_forecast is not None:
        return WeatherForecastOut(**weather_forecast.as_dict())
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@weather_forecast_router.get('/get-all', response_model=list[WeatherForecastOut])
def get_all(date_from: Date, date_to: Date, db: WeatherForecastHolder = Depends(database)):
    data = db.get_between(date_from, date_to)
    return [WeatherForecastOut(**item.as_dict()) for item in data]


@weather_forecast_router.post('/add', response_model=WeatherForecastOut)
def add(new_weather_forecast: WeatherForecastIn, db: WeatherForecastHolder = Depends(database)):
    if db.add(**new_weather_forecast.model_dump()):
        return WeatherForecastOut(**db.get(new_weather_forecast.date).as_dict())
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail='A weather forecast for the specified date already exists')


@weather_forecast_router.put('/update', response_model=WeatherForecastOut)
def update(weather_forecast: WeatherForecastIn, db: WeatherForecastHolder = Depends(database)):
    if db.update(**weather_forecast.model_dump()):
        return WeatherForecastOut(**db.get(weather_forecast.date).as_dict())
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@weather_forecast_router.delete('/delete')
def delete(date: Date, db: WeatherForecastHolder = Depends(database)):
    if db.delete(date):
        return status.HTTP_200_OK
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
