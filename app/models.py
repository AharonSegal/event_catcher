from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Event(BaseModel):
    event_type: str
    source: str
    timestamp: Optional[datetime] = None
    payload: dict
