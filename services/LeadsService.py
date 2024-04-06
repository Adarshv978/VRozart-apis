from typing import List
from fastapi import Depends
from models.vrozart import Leads
from reposetories.LeadsRepositry import LeadsRepositry

class LeadsService:
    def __init__(self, leads_repository: LeadsRepositry = Depends()):
        self.leads_repository = leads_repository

    def get_all_leads(self) -> List[Leads]:
        return self.leads_repository.get_all_leads()

  
    def insert_lead(self, leads_body: Leads)->Leads:
        print("Lead Body---------", leads_body)
        return self.leads_repository.insert_lead(leads_body)   
    
    def search_lead(self,query)->List[Leads]:
        print("Lead Body---------", query)
        return self.leads_repository.search_lead(query)  
