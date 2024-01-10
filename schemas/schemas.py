from pydantic import BaseModel
from fastapi import Query
from typing import Optional


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
    username: str
    full_name: str
    email: Optional[str]
    phone_number: str
    real_estate_name: str
    phone: str
    region_name: Optional[str]
    city_name: Optional[str]
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
