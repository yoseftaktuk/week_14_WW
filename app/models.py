from pydantic import BaseModel, Field


class Info(BaseModel):
    weapon_id: str
    weapon_name: str
    weapon_type: str
    range_km: int
    weight_kg: float
    manufacturer: str = Field(default=None) 
    origin_country: str
    storage_location: str
    year_estimated: int

