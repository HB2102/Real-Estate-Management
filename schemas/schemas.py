from pydantic import BaseModel
from fastapi import Query
from typing import Optional
import datetime


class UserBase(BaseModel):
    username: str
    password: str
    full_name: str
    email: Optional[str]
    phone_number: str
    real_estate_name: str
    phone: str
    region_id: int
    city_id: int
    street_address: str


class UserDisplay(BaseModel):
    full_name: str
    email: Optional[str]
    phone_number: str
    real_estate_name: str
    phone: str
    region_name_id: Optional[int]
    city_name_id: Optional[int]
    street_address: str

    class Config:
        from_attributes = True


class UserDisplayFull(BaseModel):
    username: str
    full_name: str
    email: Optional[str]
    phone_number: str
    real_estate_name: str
    phone: str
    region_name: str
    city_name: str
    street_address: str

    class Config:
        from_attributes = True


class AdminUserDisplay(BaseModel):
    id: int
    username: str
    full_name: str
    email: Optional[str]
    phone_number: str
    real_estate_name: str
    phone: str
    region_name: str
    city_name: str
    street_address: str

    class Config:
        from_attributes = True


class UserAuth(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True


class RegionDisplay(BaseModel):
    id: int
    region_name: str

    class Config:
        from_attributes = True


class CityDisplay(BaseModel):
    id: int
    city_name: str

    class Config:
        from_attributes = True


class AssetTypeDisplay(BaseModel):
    id: int
    asset_type: str

    class Config:
        from_attributes = True


class BargainTypeDisplay(BaseModel):
    id: int
    bargain_type: str

    class Config:
        from_attributes = True


class NoticeBase(BaseModel):
    title: str
    region_id: int
    city_id: int
    substruction: Optional[int]
    propertyـsize: Optional[int]
    number_of_floors: Optional[int]
    number_of_house_units: Optional[int]
    floor: Optional[int]
    room_number: Optional[int]
    area: Optional[str]
    neighbourhood: Optional[str]
    address: Optional[str]
    prepayment: Optional[int]
    price: Optional[int]
    description: Optional[str]
    asset_type_id: int
    bargain_type_id: int
    id_for_real_estate: int


class NoticeDisplay(BaseModel):
    user: UserDisplay
    title: str
    region_id: int
    city_id: int
    substruction: Optional[int]
    propertyـsize: Optional[int]
    number_of_floors: Optional[int]
    number_of_house_units: Optional[int]
    floor: Optional[int]
    room_number: Optional[int]
    area: Optional[str]
    neighbourhood: Optional[str]
    address: Optional[str]
    prepayment: Optional[int]
    price: Optional[int]
    description: Optional[str]
    asset_type_id: int
    bargain_type_id: int

class NoticeDisplayFull(BaseModel):
    user: UserDisplayFull
    title: str
    region_id: int
    city_id: int
    substruction: Optional[int]
    propertyـsize: Optional[int]
    number_of_floors: Optional[int]
    number_of_house_units: Optional[int]
    floor: Optional[int]
    room_number: Optional[int]
    area: Optional[str]
    neighbourhood: Optional[str]
    address: Optional[str]
    prepayment: Optional[int]
    price: Optional[int]
    description: Optional[str]
    asset_type_id: int
    bargain_type_id: int
    created_at: datetime.datetime
    id_for_real_estate: int

    class Config:
        from_attributes = True

class NoticeDisplayFull(BaseModel):
    user: AdminUserDisplay
    title: str
    region_id: int
    city_id: int
    substruction: Optional[int]
    propertyـsize: Optional[int]
    number_of_floors: Optional[int]
    number_of_house_units: Optional[int]
    floor: Optional[int]
    room_number: Optional[int]
    area: Optional[str]
    neighbourhood: Optional[str]
    address: Optional[str]
    prepayment: Optional[int]
    price: Optional[int]
    description: Optional[str]
    asset_type_id: int
    bargain_type_id: int
    created_at: datetime.datetime
    id_for_real_estate: int

    class Config:
        from_attributes = True
