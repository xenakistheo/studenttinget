from fastapi import FastAPI
from cases import router as case_router
from pdfs import router as pdf_router


# Initialize FastAPI app
app = FastAPI()


#Include routers
app.include_router(case_router, prefix="/cases", tags=["cases"])
app.include_router(pdf_router, prefix="/pdfs", tags=["pdfs"])