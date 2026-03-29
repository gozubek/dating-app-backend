from pydantic import BaseModel

class User(BaseModel):
    name: str
    birth_year: int
    birth_month: int
    birth_day: int
    birth_hour: int
    birth_minute: int
    timezone_offset: int = 0