import datetime as _dt
from typing import Optional
from pydantic import BaseModel, ConfigDict

class _BaseContact(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None

class CreateContact(_BaseContact):
    pass

class UpdateContact(_BaseContact):
    pass

class Contact(_BaseContact):
    id: int
    date_created: _dt.datetime

    model_config = ConfigDict(from_attributes=True)
