from pydantic import BaseModel
from typing import List, Dict
from datetime import datetime


# class Leads(BaseModel):
#     name: str 
#     company: str
#     lead_scores: int
#     phone_number: str
#     location: str
#     tags: List[str]
#     create_date: datetime

class Leads(BaseModel):
    name: str 
    company: str
    lead_scores: int
    phone_number: str
    location: str
    tags: List[str]
    create_date:  datetime



class Insert_leads(BaseModel):
    statuse: str
    statuse_code: str
    data: Dict



