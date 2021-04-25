from requests import get

API_BASE_URL = "https://www.jma.go.jp/bosai/forecast"


def _get_json(url: str, **kwargs):
    response = get(url, **kwargs)
    response.raise_for_status()
    return response.json()


def get_forecast(city_code: str):
    endpoint = f"/data/forecast/{city_code}.json"
    return _get_json(f"{API_BASE_URL}{endpoint}")


def get_overview(city_code: str):
    endpoint = f"/data/overview_forecast/{city_code}.json"
    res_json = _get_json(f"{API_BASE_URL}{endpoint}")
    return res_json
