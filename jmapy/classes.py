from dataclasses import dataclass
from datetime import datetime


@dataclass
class Forecast:
    datetime: datetime

    pass


@dataclass
class OverView:
    publishingOffice: str
    reportDatetime: datetime
    targetArea: str
    headlineText: str
    text: str


@dataclass
class Weather:
    is_week: bool
    publishingOffice: str
    reportDatetime: datetime
    forecasts: list
