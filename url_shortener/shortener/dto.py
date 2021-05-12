from typing import Optional
from pydantic import BaseModel, Field, validator


class CreateNewLinkDto(BaseModel):
    original_url: str = Field(min_length=10, max_length=200)
    days_to_expire: Optional[int] = 90

    @validator('days_to_expire')
    def should_be_between_1_and_365(cls, v):
        if 1 <= v <= 365:
            return v
        raise ValueError('days_to_expire should be between 1 and 365')

    @validator('original_url')
    def should_start_with_http(cls, v):
        if v.startswith(('http://', 'https://')):
            return v
        raise ValueError('links should start with http/https://')
