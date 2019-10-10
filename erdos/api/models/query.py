# coding: utf-8
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class RawQuery:
    @staticmethod
    def serialize(obj):
        converted = {}
        for key in obj.keys():
            converted[key] = str(obj[key])

        return converted

    @staticmethod
    def fetch(query):
        try:
            _q = text(query)
            result = db.engine.execute(_q)
            d = [RawQuery.serialize(row) for row in result]
            return d
        except Exception as e:
            return []
