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


class AttomRec(db.Model):
    __tablename__ = 'attom_rec'
    __table_args__ = (
        Index('Grantee', 'Grantee', 'MailAddressRaw'),
        Index('MailAddressRaw', 'MailAddressRaw', 'Grantee'),
        Index('SitusStateCountyFIPS', 'SitusStateCountyFIPS', 'RecordingDate')
    )
    PID = Column(Integer)
    pid = sqlalchemy.orm.synonym('PID') # alias
    DID = Column(Integer, primary_key=True)
    did = sqlalchemy.orm.synonym('DID')  # alias
    SitusStateCountyFIPS = Column(String(100))
    DocumentNumber = Column(String(255))
    Book = Column(String(255))
    Page = Column(String(255))
    DocumentDate = Column(Date)
    FilingDate = Column(String(255))
    RecordingDate = Column(String(255), index=True)
    DocumentCategoryType = Column(String(255))
    DocumentTypeDescription = Column(String(255))
    MultiParcel = Column(String(255))
    ArmsLengthTransfer = Column(String(255))
    Legal = Column(String(255))
    Borrower = Column(String(255))
    Grantor = Column(String(255))
    Grantee = Column(String(255))
    LenderName = Column(String(255))
    CleanLenderName = Column(String(255))
    ParentLenderName = Column(String(255))
    MergerParentName = Column(String(255))
    PartialInterest = Column(String(255))
    SalePrice = Column(Integer)
    LoanRateTypeDescription = Column(String(255))
    LoanTypeDescription = Column(String(255))
    NewLoan1Amount = Column(Integer)
    NewLoan2Amount = Column(Integer)
    NewLoanDocumentNumber = Column(String(255))
    NewLoanInterestRate = Column(Numeric(5, 3))
    CreateDate = Column(Date)
    LastUpdated = Column(Date)
    PublicationDate = Column(Date)
    ProcessIndicator = Column(String(255))
    InMedianRange = Column(BIT(1))
    ForeclosureAuctionSale = Column(BIT(1))
    InvestorBulkBuy = Column(BIT(1))
    AbsentOwner = Column(BIT(1))
    DistressCircumstanceDescription = Column(String(255))
    SaleTermsDescription = Column(String(255))
    SaleTypeDescription = Column(String(255))
    TransferTypeDescription = Column(String(255))
    RTUniqueFCIdentifier = Column(Integer)
    AVMatDocRecordingDate = Column(String(255))
    SourceCountyName = Column(String(255))
    SourceMunicipalityName = Column(String(255))
    DocumentNumberFormatted = Column(String(255))
    APNOriginal = Column(String(255))
    SiteAddressRaw = Column(String(255))
    MailAddressRaw = Column(String(255))
    MailAddressHouseNumber = Column(String(255))
    MailAddressFraction = Column(String(255))
    MailAddressDirection = Column(String(255))
    MailAddressStreetName = Column(String(255))
    MailAddressSuffix = Column(String(255))
    MailAddressPostDirection = Column(String(255))
    MailAddressUnitPrefix = Column(String(255))
    MailAddressUnitValue = Column(String(255))
    MailCity = Column(String(255))
    MailState = Column(String(255))
    MailZip = Column(String(255))
    MailZip4 = Column(String(255))
    MailCRRT = Column(String(255))
    Quitclaim = Column(BIT(1))
    LegalBlock = Column(String(255))
    LegalLot = Column(String(255))
    LegalPlatBook = Column(String(255))
    LegalPlatPage = Column(String(255))
    LegalRange = Column(String(255))
    LegalSection = Column(String(255))
    LegalSubDivision = Column(String(255))
    LegalTownship = Column(String(255))
    LegalTract = Column(String(255))
    LegalUnit = Column(String(255))