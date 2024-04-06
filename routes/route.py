from fastapi import APIRouter, Depends, Query, HTTPException
from models.vrozart import Leads, Insert_leads
from config.Database import get_db_connection
from schema.schema import list_serial
from bson import ObjectId
from typing import List
from reposetories.LeadsRepositry import LeadsRepositry
from services.LeadsService import LeadsService
from pymongo.errors import OperationFailure


router = APIRouter()

db = get_db_connection()

collection = db.leads

# Get Leads Route
@router.get('/', response_model=List[Leads])
async def get_leads(service: LeadsService = Depends()):
    return service.get_all_leads()

# Post Lead Route
@router.post(
        "/",
        response_model=List[Insert_leads]
             )
async def post_leads(
    lead: Leads,
    leadsService: LeadsService = Depends(),
):
    return leadsService.insert_lead(lead)

# Search Lead Route
@router.get("/search/")
async def search_leads(query: str, service: LeadsService = Depends()):
    search_leads = service.search_lead(query)
    return search_leads