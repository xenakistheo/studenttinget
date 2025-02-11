from fastapi import APIRouter
from supabase import create_client, Client
import fitz  # PyMuPDF
import pdfplumber
import io
import requests
import os
from supabase_client import create_supabase_client
from fastapi import Query
from dotenv import load_dotenv


load_dotenv()

SUPABASE_URL = os.getenv("NEXT_PUBLIC_SUPABASE_URL")
SUPABASE_KEY = os.getenv("NEXT_PUBLIC_SUPABASE_ANON_KEY")
AUTH_EMAIL = os.getenv("AUTH_EMAIL")
AUTH_PASSWORD = os.getenv("AUTH_PASSWORD")

router = APIRouter()

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Authenticate user
auth_response = supabase.auth.sign_in_with_password({"email": AUTH_EMAIL, "password": AUTH_PASSWORD})

# Get the session token
if auth_response and auth_response.session:
    access_token = auth_response.session.access_token
    print("Authenticated successfully!")

    # Use the access token in authorized requests
    headers = {"Authorization": f"Bearer {access_token}"}

    # Example: Fetch user data with the authenticated session
    user_response = supabase.auth.get_user(access_token)
    print(user_response)

else:
    print("Authentication failed!")


def extract_text_from_pdf(pdf_content: bytes) -> str:
    """Extract text from a PDF file using pdfplumber."""
    text = ""
    with pdfplumber.open(io.BytesIO(pdf_content)) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

@router.post("/process_pdfs")
def process_pdfs():
    """Fetch PDFs from Supabase Storage, extract text, and store it in the database."""
    response = supabase.storage.from_("politikk").list("Aktiv/plattformer")
    print("\n\n\n ____________ \n\n\n")
    if not response:
        return {"message": "No PDFs found"}

    for pdf_file in response:
        print(pdf_file['name'])
        pdf_url = f"{SUPABASE_URL}/storage/v1/object/public/politikk/Aktiv/plattformer/{pdf_file['name']}"
        
        pdf_response = requests.get(pdf_url)
        if pdf_response.status_code != 200:
            continue

        extracted_text = extract_text_from_pdf(pdf_response.content)

        # Store the extracted text in Supabase
        supabase.table("pdf_texts").insert({
            "pdf_name": pdf_file['name'],
            "pdf_url": pdf_url,
            "extracted_text": extracted_text
        }).execute()

    return {"message": "PDFs processed and stored successfully"}


@router.get("/search_pdfs")
def search_pdfs(query: str = Query(...)):
    """Search for PDFs containing the query."""
    response = supabase.table("pdf_texts").select("*").ilike("extracted_text", f"%{query}%").execute()
    
    results = response.data if response.data else []
    
    return {"results": results}