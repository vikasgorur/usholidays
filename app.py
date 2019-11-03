from datetime import datetime, date
from typing import List, Dict

from flask import Flask
from flask.json import JSONEncoder, jsonify

import usholidays


class DateJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, date):
            return o.isoformat()

        return super().default(o)


app = Flask(__name__)
app.json_encoder = DateJSONEncoder


def holidays_as_list(year: int) -> List[Dict]:
    holidays = usholidays.for_year(year)
    return [
        {"name": k, "date": v}
        for k, v in holidays.items()
    ]


@app.route("/<year>")
def holidays(year: str):
    pass


@app.route("/<year>.json")
def holidays_json(year: str):
    return jsonify(holidays_as_list(int(year)))


@app.route('/')
def root():
    return holidays_json(str(datetime.now().year))