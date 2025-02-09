from pydantic import BaseModel
from typing import Optional, Dict, List, Union

class User(BaseModel):
    name: str
    email: str
    password: str

class CompanySchema(BaseModel):
    company_name: Optional[str]
    location: Optional[str]
    started: Optional[int]
    organization_number: Optional[int]
    type: Optional[str]
    productservicesolution: Optional[str]
    employees: Optional[int]  
    revenue_2023: Optional[int]
    sector: Optional[str]
    origin: Optional[str]
    collaboration: Optional[str]
    nfr_program: Optional[str]
    project_title: Optional[str]
    period: Optional[str]
    amount_mnok: Optional[float]  
    nfr_projects: Optional[List[Dict[str, Union[str, float]]]]


class VedtakSchema(BaseModel):
    saksnummer: Optional[str]
    aarstall: Optional[int]
    sakstittel: Optional[str]
    kategori: Optional[str]
    underkategori_organisasjon: Optional[str]
    kategori2: Optional[str]
    underkategori: Optional[str]
    sakstype: Optional[str]
    status: Optional[str]
    stikkord: Optional[str]
    kommentar: Optional[str]
    tema: Optional[str]
    kom3: Optional[str]

