from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.participants import router as participants_router
from database import create_tables

app = FastAPI(title="Bike-Drone API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    create_tables()

app.include_router(participants_router, prefix="/participants")

@app.get("/")
def root():
    return {"message": "Bike-Drone API is running 🚴"}