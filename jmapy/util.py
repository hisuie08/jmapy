from datetime import datetime


def datetime_parser(date_string: str):
    return datetime.fromisoformat(date_string)
