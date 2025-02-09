from pydantic import BaseModel
from typing import Optional, Dict, List, Union

class User(BaseModel):
    name: str
    email: str
    password: str

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

