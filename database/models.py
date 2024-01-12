from database.database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean


# USER TABLE ============================================================================================
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, index=True, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    full_name = Column(String)
    email = Column(String)
    phone_number = Column(String)
    real_estate_name = Column(String)
    phone = Column(String)
    region_id = Column(Integer, ForeignKey('region.id'))
    city_id = Column(Integer, ForeignKey('city.id'))
    street_address = Column(String)
    is_admin = Column(Boolean)


# NOTICE TABLE ============================================================================================
class Notice(Base):
    __tablename__ = 'notice'
    id = Column(Integer, index=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    title = Column(String)
    region_id = Column(Integer, ForeignKey('region.id'))
    city_id = Column(Integer, ForeignKey('city.id'))
    is_available = Column(Boolean)
    created_at = Column(DateTime)
    unavailable_date = Column(DateTime)
    substruction = Column(Integer)
    propertyـsize = Column(Integer)
    number_of_floors = Column(Integer)
    number_of_house_units = Column(Integer)
    floor = Column(Integer)
    room_number = Column(Integer)
    area = Column(String)
    neighbourhood = Column(String)
    address = Column(String)
    prepayment = Column(Integer)
    price = Column(Integer)
    description = Column(String)
    asset_type_id = Column(Integer, ForeignKey('asset_type.id'))
    bargain_type_id = Column(Integer, ForeignKey('bargain_type.id'))
    id_for_real_estate = Column(Integer)


# NOTICE PICTURE TABLE ============================================================================================
class NoticePicture(Base):
    __tablename__ = 'notice_picture'
    id = Column(Integer, index=True, primary_key=True)
    notice_id = Column(Integer, ForeignKey('notice.id'))
    picture_path = Column(String)


# ASSET TYPE ============================================================================================
class AssetType(Base):
    __tablename__ = 'asset_type'
    id = Column(Integer, index=True, primary_key=True)
    asset_type = Column(String)


# BARGAIN TYPE ============================================================================================
class BargainType(Base):
    __tablename__ = 'bargain_type'
    id = Column(Integer, index=True, primary_key=True)
    bargain_type = Column(String)


# REGION TABLE ============================================================================================
class Region(Base):
    __tablename__ = 'region'
    id = Column(Integer, index=True, primary_key=True)
    region_name = Column(String, unique=True)


# CITY TABLE ============================================================================================
class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, index=True, primary_key=True)
    city_name = Column(String)
    region_id = Column(Integer, ForeignKey('region.id'))


