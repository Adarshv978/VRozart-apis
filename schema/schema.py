def individual_serial(leads)->dict:
    return {
        "id": str(leads["_id"]),
        "name": str(leads["name"]),
        "company": str(leads["company"]),
        "lead_scores": int(leads["lead_scores"]),
        "phone_number": str(leads["phone_number"]),
        "location": str(leads["location"]),
        "tags": list(leads["tags"]),
        "create_date": leads["create_date"].isoformat()  # Assuming create_date is a datetime object
    }

def list_serial(leads)->list:
    return[individual_serial(lead) for lead in leads]