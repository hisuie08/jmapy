import json
from .classes import *
from .util import *


def parse_overview(json_dict) -> OverView:
    publishingOffice = json_dict.get("publishingOffice")
    reportDatetime = datetime_parser(json_dict.get("reportDatetime"))
    targetArea = json_dict.get("targetArea")
    headlineText = json_dict.get("headlineText")
    text = json_dict.get("text")
    return OverView(publishingOffice, reportDatetime, targetArea, headlineText, text)


def parse_forecast(city_code, json_dict, is_week: bool = False):
    index = 0 if is_week else 1
    parsed_json = json_dict[index]
    timedefines = parsed_json.get("timeDefines")
    for timedefine in timedefines:
        forecast_per_day = _parse_forecast_per_day(city_code,
                                                   parsed_json, timedefines.index(timedefine))
    return Forecast()


def _parse_forecast_per_day(city_code, parsed_json, index: int):
    date = datetime_parser(parsed_json.get(
        "timeSeries").get("timeDefines").get(index))

    return Forecast()
