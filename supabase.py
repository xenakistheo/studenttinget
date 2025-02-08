from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in the .env file.")

print(f"Connecting to Supabase: {SUPABASE_URL}")

def create_supabase_client():

    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    return supabase

