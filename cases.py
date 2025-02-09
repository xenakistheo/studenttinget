from fastapi import APIRouter, HTTPException
from supabase_client import create_supabase_client
from models import VedtakSchema
import logging

router = APIRouter()
supabase = create_supabase_client()

#companies -> databaseDEMO

@router.get("/")
def get_companies():
    try:
        response = supabase.table("databaseDEMO").select("*").execute()

        # Check for errors
        if hasattr(response, "error") and response.error:
            print("Error fetching table:", response.error)
            return None

        # Access the data
        if hasattr(response, "data"):
            return response.data

        print("No data attribute in response")
        return None

    except Exception as e:
        print("Unhandled exception while fetching cases:", e)
        return None

@router.get("/{case_id}")
def get_company(case_id: int):

    try:
        response = supabase.table("databaseDEMO").select("*").eq("saksnummer", case_id).execute()
        if hasattr(response, "error") and response.error:
            logging.error(f"Error fetching case: {response.error}")
            raise HTTPException(status_code=500, detail=response.error.message)
        
        if hasattr(response, "data") and response.data:
            return response.data[0]
        
        logging.warning(f"Case with ID {case_id} not found")
        raise HTTPException(status_code=404, detail="Company not found")
    
    except Exception as e:
        logging.error(f"Unhandled exception while fetching case: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred while fetching the case: {str(e)}")


@router.post("/")
def create_company(case: dict):

    try:
        response = supabase.table("databaseDEMO").insert(case).execute()
        if hasattr(response, "error") and response.error:
            logging.error(f"Error creating case: {response.error}")
            raise HTTPException(status_code=500, detail=response.error.message)
        
        return {"message": "Case created successfully", "case_id": response.data[0]["saksnummer"]}
    
    except Exception as e:
        logging.error(f"Unhandled exception while creating case: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred while creating the case: {str(e)}")


@router.delete("/{case_id}")
def delete_company(case_id: int):

    try:
        response = supabase.table("databaseDEMO").delete().eq("saksnummer", case_id).execute()
        if hasattr(response, "error") and response.error:
            logging.error(f"Error deleting case: {response.error}")
            raise HTTPException(status_code=500, detail=response.error.message)
        
        if hasattr(response, "data") and not response.data:
            logging.warning(f"Case with ID {case_id} not found")
            raise HTTPException(status_code=404, detail="Case not found")
        
        return {"message": "Case deleted successfully"}
    
    except Exception as e:
        logging.error(f"Unhandled exception while deleting case: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred while deleting the case: {str(e)}")
    
@router.patch("/{case_id}")
def update_company(case_id: int, case_update: VedtakSchema):
    """
    Update a company's details by its ID.
    """
    try:
        # Filter out fields that are None to avoid overwriting with null
        update_data = {
            key: value
            for key, value in case_update.dict().items()
            if value is not None and value != "string" and value != 0
        }

        if not update_data:
            raise HTTPException(status_code=400, detail="No valid fields provided for update")

        # Perform the update
        response = supabase.table("databaseDEMO").update(update_data).eq("saksnummer", case_id).execute()

        # Check for errors
        if hasattr(response, "error") and response.error:
            logging.error(f"Error updating company: {response.error}")
            raise HTTPException(status_code=500, detail=response.error.message)

        # Check if the company exists
        if hasattr(response, "data") and not response.data:
            logging.warning(f"Case with ID {case_id} not found")
            raise HTTPException(status_code=404, detail="Case not found")

        return {"message": "Case updated successfully", "updated_data": response.data[0]}

    except Exception as e:
        logging.error(f"Unhandled exception while updating case: {e}")
        raise HTTPException(status_code=500, detail=f"An error occurred while updating the case: {str(e)}")
