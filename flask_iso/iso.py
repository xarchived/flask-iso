from datetime import date
from typing import Union

from flask import Blueprint, Flask
from flask.json import JSONEncoder


class CustomJSONEncoder(JSONEncoder):
    def default(self, obj):
        try:
            if isinstance(obj, date):
                return obj.isoformat()
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


class Iso(object):
    _app: Union[Flask, Blueprint]

    def __init__(self, app: Union[Flask, Blueprint] = None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Union[Flask, Blueprint]) -> None:
        self._app = app
        app.json_encoder = CustomJSONEncoder
