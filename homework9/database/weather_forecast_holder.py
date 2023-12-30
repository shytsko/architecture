from datetime import date as Date
from dataclasses import dataclass
from typing import Any


@dataclass
class WeatherForecastDBModel:
    date: Date
    temperature_c: int

    @property
    def temperature_f(self):
        return 32 + int(self.temperature_c / 0.5556)

    def as_dict(self):
        return {'date': self.date, 'temperature_c': self.temperature_c, 'temperature_f': self.temperature_f}


class WeatherForecastHolder:
    def __init__(self):
        self._data: dict[Date, WeatherForecastDBModel] = {}

    def add(self, date: Date, temperature_c: int) -> bool:
        if date in self._data:
            return False

        self._data[date] = WeatherForecastDBModel(date, temperature_c)
        return True

    def get(self, date: Date) -> WeatherForecastDBModel | None:
        return self._data.get(date)

    def get_between(self, date_from: Date, date_to: Date) -> list[WeatherForecastDBModel]:
        return [weather_forecast for date, weather_forecast in self._data.items() if date_from <= date <= date_to]

    def update(self, date: Date, temperature_c: int) -> bool:
        if date not in self._data:
            return False

        self._data[date] = WeatherForecastDBModel(date, temperature_c)
        return True

    def delete(self, date: Date) -> bool:
        if date not in self._data:
            return False

        self._data.pop(date)
        return True

    def __call__(self):
        return self
