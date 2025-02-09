from fastapi import FastAPI
from cases import router as case_router




# Initialize FastAPI app
app = FastAPI()


#Include routers
app.include_router(case_router, prefix="/cases", tags=["cases"])