from flask_sqlalchemy import SQLAlchemy
from utility import dump_date, CustomModel

db = SQLAlchemy()


class RecentSalesResults(CustomModel):
    """
    get the recent sales data
    """

    def __init__(self):
        super(RecentSalesResults, self).__init__()
        # input variable for the query
        self.pid = 0

    def _build_query(self):
        """query for database"""
        return """
        select *
        from attom_recent_sales
        where fips in ('08001')
        limit 10;
        """.format(pid=self.pid)

    def _serialize(self, row):
        """serialize RowProxy from sqlalchemy.engine.result.ResultProxy"""

        converted = {}
        for key in row.keys():
            converted[key] = str(row[key])
        return converted
