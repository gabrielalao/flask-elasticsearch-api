from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from utility import dump_date, CustomModel

db = SQLAlchemy()


class Cass(CustomModel):
    """
    get the CASS data for a given PID
    """

    def __init__(self, pid):
        super(Cass, self).__init__()
        # input variable for the query
        self.pid = pid

    def _build_query(self):
        """query for database"""
        return """
        SELECT * FROM cass_sfr_201709_reg WHERE pid={pid}
        UNION
        SELECT * FROM cass_sfr_201708_reg WHERE pid={pid}
        UNION
        SELECT * FROM cass_sfr_201707_reg WHERE pid={pid}
        """.format(pid=self.pid)

    def _serialize(self, row):
        """serialize RowProxy from sqlalchemy.engine.result.ResultProxy"""

        # converted = {}
        # for key in row.keys():
        #     converted[key] = str(row[key])
        # return converted

        return {
            'pid': row.pid,
            'fips': row.fips,
            'vacant': row.vacant,
            'date': dump_date(row.ds),
            'dpv': {
                'dpv_match_code': row.dpv_match_code,
                'dpv_footnotes': row.dpv_footnotes,
                'dpv_cmra': row.dpv_cmra,
                'dpv_vacant': row.dpv_vacant,
            },
            'property_address': {
                'delivery_line_1': row.delivery_line_1,
                'last_line': row.last_line,
                'city': row.city_name,
                'state': row.state_abbreviation,
                'zip': row.zipcode
            }
        }
