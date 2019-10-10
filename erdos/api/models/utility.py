from abc import ABCMeta, abstractmethod

from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def dump_date(value):
    """Deserialize datetime object into string form for JSON processing."""
    return value.strftime("%Y-%m-%d") if value else None


class CustomModel(object):
    __metaclass__ = ABCMeta

    def generate_results(self):
        """returns JSON"""
        result = db.engine.execute(self._build_query())
        output = [self._serialize(row) for row in result]
        return jsonify(output)

    @abstractmethod
    def _serialize(self, row):
        pass

    @abstractmethod
    def _build_query(self):
        pass
