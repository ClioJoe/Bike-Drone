from pydantic import BaseModel
from typing import Optional

class Participant(BaseModel):
    firstName: str
    lastName: str
    stravaScore: int
    weight: float
    level: str
    bikeStatus: str
    needs: Optional[str] = ""
    droneConsent: bool