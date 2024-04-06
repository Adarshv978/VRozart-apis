from fastapi import Depends
from config.Database import (get_db_connection)
from models.vrozart import Leads
from typing import Dict, List
from datetime import datetime



class LeadsRepositry:
    def __init__(self):
        self.db = get_db_connection()  # Call get_db_connection to get the database connection

    def get_all_leads(self):
        return list(self.db.leads.find())  
    
   
    def insert_lead(self, leads_body: Leads) -> List[Dict]:
        # Insert lead into database
        params = {
            "name": leads_body.name,
            "company": leads_body.company,
            "lead_scores": leads_body.lead_scores,
            "phone_number": leads_body.phone_number,
            "location": leads_body.location,
            "tags": leads_body.tags,
            "create_date": leads_body.create_date
        }
        result = self.db.leads.insert_one(params)

        print("Result------>", result)
        # Convert ObjectId to string
        params['_id'] = str(params['_id'])
        responce = {
            'statuse': "OK",
            'statuse_code': "200",
            'data': params
        }
        print("Responce ---->", responce)

        return [responce]

    def search_lead(self,query):
        print("The Query is", query)
        results = list(self.db.leads.find({"name": {"$regex": f".*{query}.*", "$options": "i"}}))
        for result in results:
            result['_id'] = str(result['_id'])
        return results
           
    

