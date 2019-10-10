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


class AttomForeclosure(db.Model):
    __tablename__ = 'attom_foreclosure'

    PID = Column(Integer, primary_key=True)
    pid = sqlalchemy.orm.synonym('PID')
    RTUniqueFCIdentifier = Column(Integer)
    JurisdictionCountyFIPS = Column(String(255))
    RecordType = Column(String(255))
    ParcelNumber = Column(String(255))
    SitusAddress = Column(String(255))
    SitusCity = Column(String(255))
    SitusState = Column(String(255))
    SitusZip = Column(Integer)
    SitusCounty = Column(String(255))
    SitusFIPS = Column(String(255))
    BorrowersNameOrOwner = Column(String(255))
    LenderName = Column(String(255))
    LenderAddress = Column(String(255))
    LenderCity = Column(String(255))
    LenderState = Column(String(255))
    LenderZip = Column(String(255))
    LenderPhone = Column(String(255))
    CleanLenderName = Column(String(255))
    ParentLenderName = Column(String(255))
    MergerParentName = Column(String(255))
    ServicerName = Column(String(255))
    ServicerAddress = Column(String(255))
    ServicerCity = Column(String(255))
    ServicerPhone = Column(String(255))
    ServicerState = Column(String(255))
    ServicerZip = Column(String(255))
    TrusteeName = Column(String(255))
    TrusteeAddress = Column(String(255))
    TrusteeCity = Column(String(255))
    TrusteeState = Column(String(255))
    TrusteeZip = Column(String(255))
    TrusteePhone = Column(String(255))
    FCDocRecordingDate = Column(Date)
    FCDocInstrumentNumber = Column(String(255))
    FCDocBookPage = Column(String(255))
    FCDocInstrumentDate = Column(Date)
    RelatedDocumentInstrumentNumber = Column(String(255))
    RelatedDocDocumentBookPage = Column(String(255))
    RelatedDocumentRecordingDate = Column(String(255))
    RecordedAuctionDate = Column(Date)
    RecordedOpeningBid = Column(Integer)
    CaseNumber = Column(String(255))
    TrusteeReferenceNumber = Column(String(255))
    Payment = Column(Integer)
    LoanNumber = Column(String(255))
    LoanMaturityDate = Column(Date)
    DefaultAmount = Column(Integer)
    OriginalLoanAmount = Column(Integer)
    PenaltyInterest = Column(Integer)
    LoanBalance = Column(Integer)
    InterestRate = Column(Numeric(5, 3))
    JudgementDate = Column(Date)
    JudgmentAmount = Column(Integer)
    AuctionCourthouse = Column(String(255))
    AuctionAddress = Column(String(255))
    AuctionCityState = Column(String(255))
    AuctionTime = Column(String(255))
    CreateDate = Column(Date)
    LastUpdated = Column(Date)
    PublicationDate = Column(Date)
    ProcessIndicator = Column(String(255))
    EstimatedValue = Column(Integer)
