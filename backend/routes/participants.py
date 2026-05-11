from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, Participant
from models.participant import Participant as ParticipantModel

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_participants(db: Session = Depends(get_db)):
    participants = db.query(Participant).order_by(Participant.stravaScore.desc()).all()
    return {"total": len(participants), "participants": [
        {
            "firstName": p.firstName,
            "lastName": p.lastName,
            "stravaScore": p.stravaScore,
            "weight": p.weight,
            "level": p.level,
            "bikeStatus": p.bikeStatus,
            "needs": p.needs,
            "droneConsent": p.droneConsent
        } for p in participants
    ]}

@router.post("/register")
def register_participant(participant: ParticipantModel, db: Session = Depends(get_db)):
    count = db.query(Participant).count()
    if count >= 50:
        return {"error": "Registration is full. Maximum 50 participants reached."}
    
    new_participant = Participant(
        firstName=participant.firstName,
        lastName=participant.lastName,
        stravaScore=participant.stravaScore,
        weight=participant.weight,
        level=participant.level,
        bikeStatus=participant.bikeStatus,
        needs=participant.needs,
        droneConsent=participant.droneConsent
    )
    db.add(new_participant)
    db.commit()
    db.refresh(new_participant)
    return {"message": "Registration successful!", "participant": participant}

@router.delete("/reset")
def reset_participants(db: Session = Depends(get_db)):
    db.query(Participant).delete()
    db.commit()
    return {"message": "All participants cleared."}

from ai.route_generator import get_surprise_routes, generate_route

@router.get("/routes")
def get_routes(level: str = "intermediate"):
    routes = get_surprise_routes(level)
    return {"routes": routes}

@router.get("/routes/generate")
def generate_single_route(level: str = "intermediate", duration: int = 60):
    route = generate_route(level, duration)
    return {"route": route}

@router.delete("/{participant_id}")
def delete_participant(participant_id: int, db: Session = Depends(get_db)):
    participant = db.query(Participant).filter(Participant.id == participant_id).first()
    if not participant:
        return {"error": "Participant not found"}
    db.delete(participant)
    db.commit()
    return {"message": "Participant deleted successfully"}