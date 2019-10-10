# coding: utf-8
from sqlalchemy import BigInteger, Column, Date, Index, Integer, Numeric, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from utility import dump_date

db = SQLAlchemy()
Base = declarative_base()
metadata = Base.metadata

"""

https://stackoverflow.com/questions/7102754/jsonify-a-sqlalchemy-result-set-in-flask

"""


class AttomTax(db.Model):
    __tablename__ = 'attom_tax'
    __table_args__ = (
        Index('search', 'SitusStateCountyFIPS', 'SFR', 'OwnerOccupiedInt', 'SquareFootage', 'YearBuilt'),
        Index('SitusStateCountyFIPS', 'SitusStateCountyFIPS', 'SFR', 'OwnerOccupiedInt')
    )

    PID = Column(Integer, primary_key=True)
    pid = sqlalchemy.orm.synonym('PID')  # alias
    sa_property_id = Column(BigInteger)
    SitusStateCountyFIPS = Column(String(10))
    JurisdictionCountyFIPS = Column(String(10))
    APNUnformatted = Column(String(100))
    APNFormatted = Column(String(255))
    SitusAddress = Column(String(255))
    SitusCity = Column(String(255))
    SitusState = Column(String(255))
    SitusZip = Column(String(255))
    SitusZip4 = Column(String(255))
    SitusCounty = Column(String(255))
    SitusHouseNumber = Column(String(255))
    SitusHouseNumberFraction = Column(String(255))
    SitusStreetName = Column(String(255))
    SitusDirection = Column(String(255))
    SitusAddressSuffix = Column(String(255))
    SitusPostDirection = Column(String(255))
    SitusUnitPrefix = Column(String(255))
    SitusUnitValue = Column(String(255))
    CombinedStatisticalArea = Column(String(255))
    MetropolitanDivision = Column(String(255))
    Longitude = Column(Numeric(10, 8))
    Latitude = Column(Numeric(11, 8))
    OccupancyStatus = Column(Integer)
    LegalDescription = Column(String(8000))
    LotNumber = Column(String(100))
    Subdivision = Column(String(100))
    Section = Column(String(100))
    Township = Column(String(100))
    Quarter = Column(String(100))
    Range = Column(String(100))
    PropertyZoning = Column(String(100))
    PropertyGroup = Column(String(100))
    PropertyType = Column(String(100))
    Bedrooms = Column(Integer)
    Bathrooms = Column(Numeric(9, 3))
    SquareFootage = Column(Integer)
    LotSize = Column(Numeric(12, 2))
    YearBuilt = Column(Integer)
    EffectiveYearBuilt = Column(Integer)
    ArchitectureDescription = Column(String(100))
    StructureDescription = Column(String(100))
    ExteriorDescription1 = Column(String(100))
    ExteriorDescription2 = Column(String(100))
    ConstructionDescription = Column(String(100))
    ContructionQuality = Column(Numeric(10, 2))
    LotDepth = Column(Integer)
    LotWidth = Column(Integer)
    FinishSquareFeet1 = Column(Integer)
    FinishSquareFeet2 = Column(Integer)
    FinishSquareFeet3 = Column(Integer)
    FinishSquareFeet4 = Column(Integer)
    AdditionsSquareFeet = Column(Integer)
    AtticSquareFeet = Column(Integer)
    BasementSquareFeet = Column(Integer)
    GarageSquareFeet = Column(Integer)
    HeatingCooling = Column(String(100))
    HeatingDetailDescription = Column(String(100))
    CoolingDetailDescription = Column(String(100))
    FirePlaceDescription = Column(String(100))
    GarageCarport = Column(String(100))
    BathroomNumberQuarter = Column(Integer)
    BathroomNumberHalf = Column(Integer)
    BathroomNumberThreeQuarter = Column(Integer)
    BathroomNumberFull = Column(Integer)
    NumberOfUnits = Column(Integer)
    RoofTypeDescription = Column(String(100))
    AirConditioning = Column(String(100))
    PoolDescription = Column(String(100))
    TaxYear = Column(Integer)
    TaxAssessedValue = Column(Integer)
    TaxImprovementValue = Column(Integer)
    TaxLandValue = Column(Integer)
    TaxImprovementPercent = Column(Integer)
    TaxAmount = Column(Integer)
    TaxDelinquentYear = Column(Integer)
    FullCashValue = Column(Integer)
    CurrentLimitValue = Column(Integer)
    MarketValue = Column(Integer)
    TaxExemptionAmountHomeowner = Column(Integer)
    TaxExemptionAmountDisabled = Column(Integer)
    TaxExemptionAmountSenior = Column(Integer)
    TaxExemptionAmountVeteran = Column(Integer)
    TaxExemptionAmountWidow = Column(Integer)
    TaxExemptionAmountOther = Column(Integer)
    TaxBillMailingAddress = Column(String(255))
    TaxBillMailingCity = Column(String(255))
    TaxBillMailingState = Column(String(255))
    TaxBillMailingZip = Column(String(255))
    TaxBillMailingZip4 = Column(String(255))
    TaxBillMailingCounty = Column(String(255))
    TaxBillMailingFIPs = Column(String(255))
    TaxBillMailingHouseNumber = Column(String(255))
    TaxBillMailingHouseNumberFraction = Column(String(255))
    TaxBillMailingStreetName = Column(String(255))
    TaxBillMailingDirection = Column(String(255))
    TaxBillMailingAddressSuffix = Column(String(255))
    TaxBillMailingPostDirection = Column(String(255))
    TaxBillMailingUnitPrefix = Column(String(255))
    TaxBillMailingUnitValue = Column(String(255))
    PrimaryOwnerNamePrefix = Column(String(255))
    PrimaryOwnerFullName = Column(String(255))
    PrimaryOwnerFirstName = Column(String(255))
    PrimaryOwnerMiddleName = Column(String(255))
    PrimaryOwnerLastName = Column(String(255))
    PrimaryOwnerNameSuffix = Column(String(255))
    PrimaryOwnerOtherPartyName = Column(String(255))
    PrimaryOwnerSpouseFirstName = Column(String(255))
    PrimaryOwnerSpouseMiddleName = Column(String(255))
    PrimaryOwnerSpouseNameSuffix = Column(String(255))
    SecondaryOwnerFullName = Column(String(255))
    SecondaryOwnerFirstName = Column(String(255))
    SecondaryOwnerMiddleName = Column(String(255))
    SecondaryOwnerLastName = Column(String(255))
    SecondryOwnerNameSuffix = Column(String(255))
    SecondaryOwnerSpouseFirstName = Column(String(255))
    SecondaryOwnerSpouseMiddleName = Column(String(255))
    OwnershipVestingRelationDescription = Column(String(255))
    TrustDescription = Column(String(255))
    SecondOwnerTypeDescription = Column(String(255))
    OwnerTypeDescription = Column(String(255))
    CreateDate = Column(Date)
    LastUpdated = Column(Date)
    PublicationDate = Column(Date)
    ProcessIndicator = Column(String(1))
    EstimatedValue = Column(Integer)
    LastSaleDate = Column(Date)
    LastSaleAmount = Column(Integer)
    PriorSaleDate = Column(Date)
    PriorSaleAmount = Column(Integer)
    OpenLoan1 = Column(Integer)
    OpenLoan2 = Column(Integer)
    OpenLoan3 = Column(Integer)
    Equity = Column(Integer)
    CalculationDate = Column(Date)
    NumberOfRooms = Column(Integer)
    NumberOfStories = Column(Integer)
    ViewDescription = Column(String(255))
    MunicipalityName = Column(String(255))
    InactiveParcelFlag = Column(String(255))
    ParcelNumberReference = Column(String(255))
    ParcelAccountNumber = Column(String(255))
    ParcelNumberAlternate = Column(String(255))
    ParcelNumberPrevious = Column(String(255))
    ParcelNumberYearChange = Column(Integer)
    ShellParcelFlag = Column(String(255))
    ApnAddedYear = Column(Integer)
    AddressCRRT = Column(String(255))
    OwnerOccupied = Column(String(255))
    UcUseCodeMuni = Column(String(255))
    CensusBlockGroup = Column(Integer)
    CensusTract = Column(Integer)
    GeoQualityCode = Column(Integer)
    MSACode = Column(Integer)
    NumberOfBathsDQ = Column(Numeric(10, 3))
    FinishSquareFeet = Column(Integer)
    SquareFeetAssessorTotal = Column(Integer)
    Acreage = Column(Numeric(10, 6))
    LotType = Column(String(255))
    StructureNumber = Column(Integer)
    FoundationDescription = Column(String(255))
    InteriorCode = Column(String(255))
    LandSlopeCode = Column(String(255))
    BuildingQualityClassCode = Column(String(255))
    ElectricAvailableCode = Column(String(255))
    Basement1Code = Column(String(255))
    PatioPorchDescription = Column(String(255))
    PatioPorchDeck1Code = Column(String(255))
    PatioSqureFeet = Column(Integer)
    PorchSquareFeet = Column(Integer)
    FuelDescription = Column(String(255))
    FirePlaceNumber = Column(Integer)
    GarageDescription = Column(String(255))
    GarageSpacesNumber = Column(Integer)
    GasAvailableCode = Column(String(255))
    SewerUsedCode = Column(String(255))
    WaterUsedCode = Column(String(255))
    NeighborhoodCode = Column(String(255))
    TopographyCode = Column(String(255))
    TaxYearAssessed = Column(Integer)
    AppraiseImprovementPercent = Column(Numeric(10, 4))
    MarketImprovementPercent = Column(Numeric(10, 4))
    AppraiseImprovementValue = Column(Integer)
    AppraiseLandValue = Column(Integer)
    PreviousAssessedValue = Column(Integer)
    MarketImprovementValue = Column(Integer)
    LandMarketValue = Column(Integer)
    AppraiseLandYear = Column(Integer)
    ExemptFlag7 = Column(String(255))
    MailingCarrierCode = Column(String(255))
    CompanyFlag = Column(String(255))
    TransferDate = Column(Date)
    DocumentNumberFormat = Column(String(255))
    MailingPrivacyCode = Column(String(255))
    TransferPrice = Column(Integer)
    SFR = Column(Integer)
    OwnerOccupiedInt = Column(Integer)
    ds = Column(String(10))

    @property
    def serialize(self):
        return {
            'id': {
                'PID': self.pid,
                'FIPS': self.SitusStateCountyFIPS
            },
            'last_sale': {
                'LastSaleDate': dump_date(self.LastSaleDate),
                'LastSaleAmount': self.LastSaleAmount
            },
            'prior_sale': {
                'PriorSaleDate': dump_date(self.PriorSaleDate),
                'PriorSaleAmount': self.PriorSaleAmount
            },
            'property_address':
                {
                    'Address': self.SitusAddress,
                    'City': self.SitusCity,
                    'State': self.SitusState,
                    'Zip': self.SitusZip,
                    'Zip4': self.SitusZip4
                },
            'mail_address': {

            },
            'primary_owner': {

            },
            'secondary_owner': {

            },
            'loan_info': {

            }
        }
