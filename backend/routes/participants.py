from fastapi import APIRouter
from models.participant import Participant
from typing import List

router = APIRouter()

# Temporary storage (will be replaced by database later)
participants_db: List[dict] = []

@router.get("/")
def get_participants():
    sorted_participants = sorted(participants_db, key=lambda x: x["stravaScore"], reverse=True)
    return {"total": len(sorted_participants), "participants": sorted_participants}

@router.post("/register")
def register_participant(participant: Participant):
    if len(participants_db) >= 50:
        return {"error": "Registration is full. Maximum 50 participants reached."}
    
    participants_db.append(participant.dict())
    return {"message": "Registration successful!", "participant": participant}

@router.delete("/reset")
def reset_participants():
    participants_db.clear()
    return {"message": "All participants cleared."}