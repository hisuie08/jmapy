from .request import *
from .classes import *
from .parser import *


class JMA:
    def __init__(self, city_code: str):
        self.city_code = city_code
        super().__init__()

    def forecast(self):
        return

    def forecast_week(self):
        return

    def overview(self):
        overview = get_overview(self.city_code)
        return parse_overview(overview)
