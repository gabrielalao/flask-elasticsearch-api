# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, DateTime, Float, ForeignKey, Index, Integer, LargeBinary, Numeric, \
    String, Table, Text, text
from sqlalchemy import UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy.dialects.mysql.types import BIT
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

db = SQLAlchemy()
Base = declarative_base()
metadata = Base.metadata


class TargetAPI(db.Model):
    """represents target_api table"""
    __tablename__ = 'target_api'
    __table_args__ = (PrimaryKeyConstraint('RTPropertyUniqueIdentifier', 'RTDocumentIdentifier'),)
    RTPropertyUniqueIdentifier = db.Column(db.Integer)
    pid = sqlalchemy.orm.synonym('RTPropertyUniqueIdentifier')
    RTDocumentIdentifier = db.Column(db.Integer)
    did = sqlalchemy.orm.synonym('RTDocumentIdentifier')
    target = db.Column(db.Integer)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    password = Column(LargeBinary)
    created_at = Column(DateTime, nullable=False)
    first_name = Column(String(30))
    last_name = Column(String(30))
    active = Column(Integer)
    is_admin = Column(Integer)


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False, unique=True)
    user_id = Column(ForeignKey(u'users.id'), index=True)

    user = relationship(u'User')


t_attom_avm = Table(
    'attom_avm', metadata,
    Column('RTPropertyUniqueIdentifier', Integer),
    Column('EstimatedValue', Integer),
    Column('Equity', Integer),
    Column('CalculationDate', Date),
    Column('EstimatedValueLow', Integer),
    Column('EstimatedValueHigh', Integer),
    Column('OpenLoanAmount1', Integer),
    Column('OpenLoanDocNumber1', String(255)),
    Column('OpenLoanAmount2', Integer),
    Column('OpenLoanDocNumber2', String(255)),
    Column('OpenLoanAmount3', Integer),
    Column('OpenLoanDocNumber3', String(255))
)

t_AVM_20170105_001_mini = Table(
    'AVM_20170105_001_mini', metadata,
    Column('RTPropertyUniqueIdentifier', Integer),
    Column('EstimatedValue', Integer),
    Column('Equity', Integer),
    Column('CalculationDate', Date),
    Column('EstimatedValueLow', Integer),
    Column('EstimatedValueHigh', Integer),
    Column('OpenLoanAmount1', Integer),
    Column('OpenLoanDocNumber1', String(255)),
    Column('OpenLoanAmount2', Integer),
    Column('OpenLoanDocNumber2', String(255)),
    Column('OpenLoanAmount3', Integer),
    Column('OpenLoanDocNumber3', String(255))
)

t_Foreclosure_20170105_001_mini = Table(
    'Foreclosure_20170105_001_mini', metadata,
    Column('RTPropertyUniqueIdentifier', Integer),
    Column('RTUniqueFCIdentifier', Integer),
    Column('JurisdictionCountyFIPS', String(255)),
    Column('RecordType', String(255)),
    Column('ParcelNumber', String(255)),
    Column('SitusAddress', String(255)),
    Column('SitusCity', String(255)),
    Column('SitusState', String(255)),
    Column('SitusZip', Integer),
    Column('SitusCounty', String(255)),
    Column('SitusFIPS', String(255)),
    Column('BorrowersNameOrOwner', String(255)),
    Column('LenderName', String(255)),
    Column('LenderAddress', String(255)),
    Column('LenderCity', String(255)),
    Column('LenderState', String(255)),
    Column('LenderZip', String(255)),
    Column('LenderPhone', String(255)),
    Column('CleanLenderName', String(255)),
    Column('ParentLenderName', String(255)),
    Column('MergerParentName', String(255)),
    Column('ServicerName', String(255)),
    Column('ServicerAddress', String(255)),
    Column('ServicerCity', String(255)),
    Column('ServicerPhone', String(255)),
    Column('ServicerState', String(255)),
    Column('ServicerZip', String(255)),
    Column('TrusteeName', String(255)),
    Column('TrusteeAddress', String(255)),
    Column('TrusteeCity', String(255)),
    Column('TrusteeState', String(255)),
    Column('TrusteeZip', String(255)),
    Column('TrusteePhone', String(255)),
    Column('FCDocRecordingDate', Date),
    Column('FCDocInstrumentNumber', String(255)),
    Column('FCDocBookPage', String(255)),
    Column('FCDocInstrumentDate', Date),
    Column('RelatedDocumentInstrumentNumber', String(255)),
    Column('RelatedDocDocumentBookPage', String(255)),
    Column('RelatedDocumentRecordingDate', String(255)),
    Column('RecordedAuctionDate', Date),
    Column('RecordedOpeningBid', Integer),
    Column('CaseNumber', String(255)),
    Column('TrusteeReferenceNumber', String(255)),
    Column('Payment', Integer),
    Column('LoanNumber', String(255)),
    Column('LoanMaturityDate', Date),
    Column('DefaultAmount', Integer),
    Column('OriginalLoanAmount', Integer),
    Column('PenaltyInterest', Integer),
    Column('LoanBalance', Integer),
    Column('InterestRate', Numeric(5, 3)),
    Column('JudgementDate', Date),
    Column('JudgmentAmount', Integer),
    Column('AuctionCourthouse', String(255)),
    Column('AuctionAddress', String(255)),
    Column('AuctionCityState', String(255)),
    Column('AuctionTime', String(255)),
    Column('CreateDate', Date),
    Column('LastUpdated', Date),
    Column('PublicationDate', Date),
    Column('ProcessIndicator', String(255)),
    Column('EstimatedValue', Integer)
)


class Recorder20170105001Mini(Base):
    __tablename__ = 'Recorder_20170105_001_mini'

    RTPropertyUniqueIdentifier = Column(Integer)
    RTDocumentIdentifier = Column(Integer, primary_key=True)
    SitusStateCountyFIPS = Column(String(100))
    DocumentNumber = Column(String(255))
    Book = Column(String(255))
    Page = Column(String(255))
    DocumentDate = Column(Date)
    FilingDate = Column(String(255))
    RecordingDate = Column(Date, index=True)
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


t_TaxAssessor_20170105_001_mini = Table(
    'TaxAssessor_20170105_001_mini', metadata,
    Column('RTPropertyUniqueIdentifier', Integer, nullable=False),
    Column('sa_property_id', BigInteger),
    Column('SitusStateCountyFIPS', String(10)),
    Column('JurisdictionCountyFIPS', String(10)),
    Column('APNUnformatted', String(100)),
    Column('APNFormatted', String(255)),
    Column('SitusAddress', String(255)),
    Column('SitusCity', String(255)),
    Column('SitusState', String(255)),
    Column('SitusZip', String(255)),
    Column('SitusZip4', String(255)),
    Column('SitusCounty', String(255)),
    Column('SitusHouseNumber', String(255)),
    Column('SitusHouseNumberFraction', String(255)),
    Column('SitusStreetName', String(255)),
    Column('SitusDirection', String(255)),
    Column('SitusAddressSuffix', String(255)),
    Column('SitusPostDirection', String(255)),
    Column('SitusUnitPrefix', String(255)),
    Column('SitusUnitValue', String(255)),
    Column('CombinedStatisticalArea', String(255)),
    Column('MetropolitanDivision', String(255)),
    Column('Longitude', Numeric(10, 8)),
    Column('Latitude', Numeric(11, 8)),
    Column('OccupancyStatus', Integer),
    Column('LegalDescription', String(8000)),
    Column('LotNumber', String(100)),
    Column('Subdivision', String(100)),
    Column('Section', String(100)),
    Column('Township', String(100)),
    Column('Quarter', String(100)),
    Column('Range', String(100)),
    Column('PropertyZoning', String(100)),
    Column('PropertyGroup', String(100)),
    Column('PropertyType', String(100)),
    Column('Bedrooms', Integer),
    Column('Bathrooms', Numeric(9, 3)),
    Column('SquareFootage', Integer),
    Column('LotSize', Numeric(12, 2)),
    Column('YearBuilt', Integer),
    Column('EffectiveYearBuilt', Integer),
    Column('ArchitectureDescription', String(100)),
    Column('StructureDescription', String(100)),
    Column('ExteriorDescription1', String(100)),
    Column('ExteriorDescription2', String(100)),
    Column('ConstructionDescription', String(100)),
    Column('ContructionQuality', Numeric(10, 2)),
    Column('LotDepth', Integer),
    Column('LotWidth', Integer),
    Column('FinishSquareFeet1', Integer),
    Column('FinishSquareFeet2', Integer),
    Column('FinishSquareFeet3', Integer),
    Column('FinishSquareFeet4', Integer),
    Column('AdditionsSquareFeet', Integer),
    Column('AtticSquareFeet', Integer),
    Column('BasementSquareFeet', Integer),
    Column('GarageSquareFeet', Integer),
    Column('HeatingCooling', String(100)),
    Column('HeatingDetailDescription', String(100)),
    Column('CoolingDetailDescription', String(100)),
    Column('FirePlaceDescription', String(100)),
    Column('GarageCarport', String(100)),
    Column('BathroomNumberQuarter', Integer),
    Column('BathroomNumberHalf', Integer),
    Column('BathroomNumberThreeQuarter', Integer),
    Column('BathroomNumberFull', Integer),
    Column('NumberOfUnits', Integer),
    Column('RoofTypeDescription', String(100)),
    Column('AirConditioning', String(100)),
    Column('PoolDescription', String(100)),
    Column('TaxYear', Integer),
    Column('TaxAssessedValue', Integer),
    Column('TaxImprovementValue', Integer),
    Column('TaxLandValue', Integer),
    Column('TaxImprovementPercent', Integer),
    Column('TaxAmount', Integer),
    Column('TaxDelinquentYear', Integer),
    Column('FullCashValue', Integer),
    Column('CurrentLimitValue', Integer),
    Column('MarketValue', Integer),
    Column('TaxExemptionAmountHomeowner', Integer),
    Column('TaxExemptionAmountDisabled', Integer),
    Column('TaxExemptionAmountSenior', Integer),
    Column('TaxExemptionAmountVeteran', Integer),
    Column('TaxExemptionAmountWidow', Integer),
    Column('TaxExemptionAmountOther', Integer),
    Column('TaxBillMailingAddress', String(255)),
    Column('TaxBillMailingCity', String(255)),
    Column('TaxBillMailingState', String(255)),
    Column('TaxBillMailingZip', String(255)),
    Column('TaxBillMailingZip4', String(255)),
    Column('TaxBillMailingCounty', String(255)),
    Column('TaxBillMailingFIPs', String(255)),
    Column('TaxBillMailingHouseNumber', String(255)),
    Column('TaxBillMailingHouseNumberFraction', String(255)),
    Column('TaxBillMailingStreetName', String(255)),
    Column('TaxBillMailingDirection', String(255)),
    Column('TaxBillMailingAddressSuffix', String(255)),
    Column('TaxBillMailingPostDirection', String(255)),
    Column('TaxBillMailingUnitPrefix', String(255)),
    Column('TaxBillMailingUnitValue', String(255)),
    Column('PrimaryOwnerNamePrefix', String(255)),
    Column('PrimaryOwnerFullName', String(255)),
    Column('PrimaryOwnerFirstName', String(255)),
    Column('PrimaryOwnerMiddleName', String(255)),
    Column('PrimaryOwnerLastName', String(255)),
    Column('PrimaryOwnerNameSuffix', String(255)),
    Column('PrimaryOwnerOtherPartyName', String(255)),
    Column('PrimaryOwnerSpouseFirstName', String(255)),
    Column('PrimaryOwnerSpouseMiddleName', String(255)),
    Column('PrimaryOwnerSpouseNameSuffix', String(255)),
    Column('SecondaryOwnerFullName', String(255)),
    Column('SecondaryOwnerFirstName', String(255)),
    Column('SecondaryOwnerMiddleName', String(255)),
    Column('SecondaryOwnerLastName', String(255)),
    Column('SecondryOwnerNameSuffix', String(255)),
    Column('SecondaryOwnerSpouseFirstName', String(255)),
    Column('SecondaryOwnerSpouseMiddleName', String(255)),
    Column('OwnershipVestingRelationDescription', String(255)),
    Column('TrustDescription', String(255)),
    Column('SecondOwnerTypeDescription', String(255)),
    Column('OwnerTypeDescription', String(255)),
    Column('CreateDate', Date),
    Column('LastUpdated', Date),
    Column('PublicationDate', Date),
    Column('ProcessIndicator', String(1)),
    Column('EstimatedValue', Integer),
    Column('LastSaleDate', Date),
    Column('LastSaleAmount', Integer),
    Column('PriorSaleDate', Date),
    Column('PriorSaleAmount', Integer),
    Column('OpenLoan1', Integer),
    Column('OpenLoan2', Integer),
    Column('OpenLoan3', Integer),
    Column('Equity', Integer),
    Column('CalculationDate', Date),
    Column('NumberOfRooms', Integer),
    Column('NumberOfStories', Integer),
    Column('ViewDescription', String(255)),
    Column('MunicipalityName', String(255)),
    Column('InactiveParcelFlag', String(255)),
    Column('ParcelNumberReference', String(255)),
    Column('ParcelAccountNumber', String(255)),
    Column('ParcelNumberAlternate', String(255)),
    Column('ParcelNumberPrevious', String(255)),
    Column('ParcelNumberYearChange', Integer),
    Column('ShellParcelFlag', String(255)),
    Column('ApnAddedYear', Integer),
    Column('AddressCRRT', String(255)),
    Column('OwnerOccupied', String(255)),
    Column('UcUseCodeMuni', String(255)),
    Column('CensusBlockGroup', Integer),
    Column('CensusTract', Integer),
    Column('GeoQualityCode', Integer),
    Column('MSACode', Integer),
    Column('NumberOfBathsDQ', Numeric(10, 3)),
    Column('FinishSquareFeet', Integer),
    Column('SquareFeetAssessorTotal', Integer),
    Column('Acreage', Numeric(10, 6)),
    Column('LotType', String(255)),
    Column('StructureNumber', Integer),
    Column('FoundationDescription', String(255)),
    Column('InteriorCode', String(255)),
    Column('LandSlopeCode', String(255)),
    Column('BuildingQualityClassCode', String(255)),
    Column('ElectricAvailableCode', String(255)),
    Column('Basement1Code', String(255)),
    Column('PatioPorchDescription', String(255)),
    Column('PatioPorchDeck1Code', String(255)),
    Column('PatioSqureFeet', Integer),
    Column('PorchSquareFeet', Integer),
    Column('FuelDescription', String(255)),
    Column('FirePlaceNumber', Integer),
    Column('GarageDescription', String(255)),
    Column('GarageSpacesNumber', Integer),
    Column('GasAvailableCode', String(255)),
    Column('SewerUsedCode', String(255)),
    Column('WaterUsedCode', String(255)),
    Column('NeighborhoodCode', String(255)),
    Column('TopographyCode', String(255)),
    Column('TaxYearAssessed', Integer),
    Column('AppraiseImprovementPercent', Numeric(10, 4)),
    Column('MarketImprovementPercent', Numeric(10, 4)),
    Column('AppraiseImprovementValue', Integer),
    Column('AppraiseLandValue', Integer),
    Column('PreviousAssessedValue', Integer),
    Column('MarketImprovementValue', Integer),
    Column('LandMarketValue', Integer),
    Column('AppraiseLandYear', Integer),
    Column('ExemptFlag7', String(255)),
    Column('MailingCarrierCode', String(255)),
    Column('CompanyFlag', String(255)),
    Column('TransferDate', Date),
    Column('DocumentNumberFormat', String(255)),
    Column('MailingPrivacyCode', String(255)),
    Column('TransferPrice', Integer)
)

t_attom_foreclosure = Table(
    'attom_foreclosure', metadata,
    Column('RTPropertyUniqueIdentifier', Integer),
    Column('RTUniqueFCIdentifier', Integer),
    Column('JurisdictionCountyFIPS', String(255)),
    Column('RecordType', String(255)),
    Column('ParcelNumber', String(255)),
    Column('SitusAddress', String(255)),
    Column('SitusCity', String(255)),
    Column('SitusState', String(255)),
    Column('SitusZip', Integer),
    Column('SitusCounty', String(255)),
    Column('SitusFIPS', String(255)),
    Column('BorrowersNameOrOwner', String(255)),
    Column('LenderName', String(255)),
    Column('LenderAddress', String(255)),
    Column('LenderCity', String(255)),
    Column('LenderState', String(255)),
    Column('LenderZip', String(255)),
    Column('LenderPhone', String(255)),
    Column('CleanLenderName', String(255)),
    Column('ParentLenderName', String(255)),
    Column('MergerParentName', String(255)),
    Column('ServicerName', String(255)),
    Column('ServicerAddress', String(255)),
    Column('ServicerCity', String(255)),
    Column('ServicerPhone', String(255)),
    Column('ServicerState', String(255)),
    Column('ServicerZip', String(255)),
    Column('TrusteeName', String(255)),
    Column('TrusteeAddress', String(255)),
    Column('TrusteeCity', String(255)),
    Column('TrusteeState', String(255)),
    Column('TrusteeZip', String(255)),
    Column('TrusteePhone', String(255)),
    Column('FCDocRecordingDate', Date),
    Column('FCDocInstrumentNumber', String(255)),
    Column('FCDocBookPage', String(255)),
    Column('FCDocInstrumentDate', Date),
    Column('RelatedDocumentInstrumentNumber', String(255)),
    Column('RelatedDocDocumentBookPage', String(255)),
    Column('RelatedDocumentRecordingDate', String(255)),
    Column('RecordedAuctionDate', Date),
    Column('RecordedOpeningBid', Integer),
    Column('CaseNumber', String(255)),
    Column('TrusteeReferenceNumber', String(255)),
    Column('Payment', Integer),
    Column('LoanNumber', String(255)),
    Column('LoanMaturityDate', Date),
    Column('DefaultAmount', Integer),
    Column('OriginalLoanAmount', Integer),
    Column('PenaltyInterest', Integer),
    Column('LoanBalance', Integer),
    Column('InterestRate', Numeric(5, 3)),
    Column('JudgementDate', Date),
    Column('JudgmentAmount', Integer),
    Column('AuctionCourthouse', String(255)),
    Column('AuctionAddress', String(255)),
    Column('AuctionCityState', String(255)),
    Column('AuctionTime', String(255)),
    Column('CreateDate', Date),
    Column('LastUpdated', Date),
    Column('PublicationDate', Date),
    Column('ProcessIndicator', String(255)),
    Column('EstimatedValue', Integer)
)



class CassSfr201704Reg(Base):
    __tablename__ = 'cass_sfr_201704_reg'
    __table_args__ = (
        Index('fips', 'fips', 'vacant'),
    )

    id = Column(BigInteger, primary_key=True)
    fips = Column(String(5))
    vacant = Column(Integer)
    ds = Column(Date)
    delivery_line_1 = Column(String(255, u'utf8mb4_bin'), server_default=text("''"))
    last_line = Column(String(255, u'utf8mb4_bin'), server_default=text("''"))
    delivery_point_barcode = Column(String(255, u'utf8mb4_bin'), server_default=text("''"))
    dpv_match_code = Column(String(255, u'utf8mb4_bin'))
    dpv_footnotes = Column(String(255, u'utf8mb4_bin'))
    dpv_cmra = Column(String(255, u'utf8mb4_bin'))
    dpv_vacant = Column(String(255, u'utf8mb4_bin'))
    active = Column(String(255, u'utf8mb4_bin'))
    footnotes = Column(String(255, u'utf8mb4_bin'))
    primary_number = Column(String(255, u'utf8mb4_bin'))
    street_name = Column(String(255, u'utf8mb4_bin'))
    street_suffix = Column(String(255, u'utf8mb4_bin'))
    city_name = Column(String(255, u'utf8mb4_bin'))
    state_abbreviation = Column(String(255, u'utf8mb4_bin'))
    zipcode = Column(String(255, u'utf8mb4_bin'))
    plus4_code = Column(String(255, u'utf8mb4_bin'))
    delivery_point = Column(String(255, u'utf8mb4_bin'))
    delivery_point_check_digit = Column(String(255, u'utf8mb4_bin'))
    record_type = Column(String(255, u'utf8mb4_bin'))
    zip_type = Column(String(255, u'utf8mb4_bin'))
    county_fips = Column(String(255, u'utf8mb4_bin'))
    county_name = Column(String(255, u'utf8mb4_bin'))
    carrier_route = Column(String(255, u'utf8mb4_bin'))
    congressional_district = Column(String(255, u'utf8mb4_bin'))
    rdi = Column(String(255, u'utf8mb4_bin'))
    elot_sequence = Column(String(255, u'utf8mb4_bin'))
    elot_sort = Column(String(255, u'utf8mb4_bin'))
    latitude = Column(String(255, u'utf8mb4_bin'))
    longitude = Column(String(255, u'utf8mb4_bin'))
    precision = Column(String(255, u'utf8mb4_bin'))
    time_zone = Column(String(255, u'utf8mb4_bin'))
    utc_offset = Column(String(255, u'utf8mb4_bin'))
    dst = Column(String(255, u'utf8mb4_bin'))


t_clustering = Table(
    'clustering', metadata,
    Column('RTPropertyUniqueIdentifier', Float(asdecimal=True)),
    Column('Label', Float(asdecimal=True))
)

t_clustering_input = Table(
    'clustering_input', metadata,
    Column('n_clusters', BigInteger),
    Column('where', Text)
)


class FIPS(Base):
    __tablename__ = 'fips'
    __table_args__ = (
        Index('state', 'state', 'county_name'),
    )

    state = Column(String(255))
    state_fips = Column(String(255))
    county_fips = Column(String(255))
    county_name = Column(String(255))
    fips_class_code = Column(String(255))
    state_county_fips = Column(String(5), primary_key=True, server_default=text("''"))
    region = Column(String(255))
    division = Column(String(255))
    county_name_experian = Column(String(255))
    exclude = Column(Integer, server_default=text("'0'"))


t_investor_id_mail = Table(
    'investor_id_mail', metadata,
    Column('id', Integer, nullable=False, index=True),
    Column('mail_address', String(255)),
    Column('mail_city', String(255)),
    Column('mail_state', String(10)),
    Column('mail_zip', String(10)),
    Column('state', String(5))
)

t_investor_id_name = Table(
    'investor_id_name', metadata,
    Column('id', Integer, nullable=False),
    Column('company_name', String(255)),
    Column('state', String(5)),
    Column('n', Integer)
)

t_investor_id_rec = Table(
    'investor_id_rec', metadata,
    Column('id', Integer, nullable=False, index=True),
    Column('RTPropertyUniqueIdentifier', Integer),
    Column('RTDocumentIdentifier', Integer),
    Column('ownership', String(10))
)

t_investor_region_exploded = Table(
    'investor_region_exploded', metadata,
    Column('region_id', BigInteger),
    Column('region_name', String(100)),
    Column('county', String(100)),
    Column('state', String(100)),
    Column('client', String(100)),
    Column('active', Integer, server_default=text("'1'"))
)


class LuigiTargetsVacant(Base):
    __tablename__ = 'luigi_targets_vacant'

    id = Column(BigInteger, nullable=False, index=True)
    update_id = Column(String(255), primary_key=True, server_default=text("''"))
    target_table = Column(String(255))
    inserted = Column(DateTime, server_default=text("CURRENT_TIMESTAMP"))


class Sample(Base):
    __tablename__ = 'sample'

    id = Column(Integer, primary_key=True)
    composer = Column(String(255))


class SfrFilter2017q1(Base):
    __tablename__ = 'sfr_filter_2017q1'
    __table_args__ = (
        Index('region_filter', 'Region', 'filter'),
        Index('fips_occ', 'SitusStateCountyFIPS', 'OwnerOccupiedInt')
    )

    RTPropertyUniqueIdentifier = Column(Integer, primary_key=True, nullable=False)
    SitusStateCountyFIPS = Column(String(5), index=True)
    SitusZip = Column(String(5))
    Region = Column(String(255), primary_key=True, nullable=False, index=True)
    OwnerOccupiedInt = Column(Integer)
    EquityPct = Column(Float)
    LengthOfOwnership = Column(Float)
    SquareFootage = Column(Integer)
    EstimatedValue = Column(Integer)
    MarketValue = Column(Integer)
    TaxAssessedValue = Column(Integer)
    filter = Column(Integer)
    filter_loo = Column(Integer)
    filter_equity = Column(Integer)
    filter_sqft = Column(Integer)
    filter_tav = Column(Integer)
    filter_est_val = Column(Integer)
    filter_est_val_pctile = Column(Integer)
    filter_zip = Column(Integer)
    filter_addy = Column(Integer, server_default=text("'1'"))
    free_pass = Column(Integer)


class SfrModelPredictions2017q1(Base):
    __tablename__ = 'sfr_model_predictions_2017q1'
    __table_args__ = (
        Index('OwnerOccupiedInt', 'OwnerOccupiedInt', 'Region', 'p_1_pctile'),
        Index('Region', 'Region', 'OwnerOccupiedInt', 'p_1_rank')
    )

    RTPropertyUniqueIdentifier = Column(Integer, primary_key=True, nullable=False)
    SitusStateCountyFIPS = Column(String(5), index=True)
    SitusZip = Column(String(5))
    Region = Column(String(255), primary_key=True, nullable=False, server_default=text("''"))
    OwnerOccupiedInt = Column(Integer)
    p_1 = Column(Float)
    p_1_rank = Column(Float(asdecimal=True))
    p_1_pctile = Column(Float(asdecimal=True))
    tranche = Column(Float(asdecimal=True))


t_sfr_zip_exclude = Table(
    'sfr_zip_exclude', metadata,
    Column('index', BigInteger, nullable=False, index=True),
    Column('region_name', String(255), server_default=text("''")),
    Column('zip', String(5), server_default=text("''")),
    Column('client', String(255), server_default=text("''"))
)
