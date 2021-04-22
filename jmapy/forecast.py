from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import List, Union

from dacite import Config, from_dict
from humps import decamelize

from areas import PopsArea, TempsArea, WeathersArea
from request import _BASE, _jma_get


def get_forecast(area_code: int | str, raw: bool = False):
    if type(raw) is not bool:
        raise TypeError(f"raw argument must be bool, not {type(raw).__name__}")
    forecast = _jma_get(
        f"{_BASE}/forecast/data/forecast/{area_code}.json")[0]
    if raw:
        return forecast
    return from_dict(Forecast, decamelize(forecast), Config({datetime: datetime.fromisoformat}))


@dataclass
class Forecast:
    publishing_office: str
    report_datetime: datetime
    time_series: List[TimeSeries]


@dataclass
class TimeSeries:
    time_defines: List[str]
    areas: List[Union[WeathersArea, TempsArea, PopsArea]]
