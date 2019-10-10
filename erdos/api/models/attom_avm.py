# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Float, ForeignKey, Index, Integer, LargeBinary, Numeric, \
    String, Table, Text, text
from sqlalchemy.dialects.mysql.types import BIT
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

db = SQLAlchemy()
Base = declarative_base()
metadata = Base.metadata


class AttomAvm(db.Model):
    __tablename__ = 'attom_avm'

    PID = Column(Integer, primary_key=True)
    pid = sqlalchemy.orm.synonym('PID')
    EstimatedValue = Column(Integer)
    Equity = Column(Integer)
    CalculationDate = Column(Date)
    EstimatedValueLow = Column(Integer)
    EstimatedValueHigh = Column(Integer)
    OpenLoanAmount1 = Column(Integer)
    OpenLoanDocNumber1 = Column(String(255))
    OpenLoanAmount2 = Column(Integer)
    OpenLoanDocNumber2 = Column(String(255))
    OpenLoanAmount3 = Column(Integer)
    OpenLoanDocNumber3 = Column(String(255))