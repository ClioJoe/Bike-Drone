# 🚴 Bike-Drone — AeroRide Drone-Guided Cycling Experience

## 📌 Project Overview
AeroRide is an innovative drone-guided cycling event where participants follow a drone through nature without knowing the route in advance. A leader equipped with a screen and headset controls the drone and guides the group from point A to B. The experience combines physical activity, technology and collective adventure.

🌐 **Live site:** [bikedrone.portalys.net](https://bikedrone.portalys.net)

---

## 👥 Team
| Name | Role | Responsibilities |
|------|------|-----------------|
| Joyce | Project Manager + Backend Dev | Coordination, planning, API, Frontend development, database, deployment |
| Joe | Tech Lead + Server + Drone |  server setup, drone integration |
| Malik | Design + Documentation | UI/UX design, project documentation |

---

## 🛠️ Tech Stack
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL (Supabase)
- **AI:** Python — surprise route generation
- **BI Dashboard:** Chart.js
- **Version Control:** GitHub
- **Project Management:** Trello, Discord

---

## 📁 Project Structure
Bike-Drone/
├── frontend/
│   ├── index.html          → Registration form
│   ├── leaderboard.html    → Participant leaderboard
│   ├── confirmation.html   → Registration confirmation
│   ├── routes.html         → AI-generated routes
│   ├── admin.html          → Admin panel
│   ├── style.css           → Global styles
│   └── script.js           → Frontend logic
├── backend/
│   ├── main.py             → FastAPI entry point
│   ├── database.py         → Supabase connection
│   ├── models/             → Data models
│   ├── routes/             → API routes
│   └── ai/                 → AI route generator
├── dashboard/
│   └── index.html          → BI analytics dashboard
├── docs/                   → Project documentation
├── README.md
└── .gitignore

---

## 🚀 How to Run

### Frontend
1. Clone the repo
2. Open `frontend/index.html` with Live Server

### Backend
```bash
cd backend
pip install -r requirements.txt
cp .env.example .env  # Add your DATABASE_URL
uvicorn main:app --reload
```

---

## 🎯 Key Features
- ✅ Participant registration (max 50 people)
- ✅ Double registration prevention
- ✅ Strava score simulation (connect button)
- ✅ Leaderboard sorted by Strava score with medals 🥇🥈🥉
- ✅ AI-generated surprise cycling routes around TalTech
- ✅ BI Dashboard with real-time analytics
- ✅ Admin panel (password protected)
- ✅ Registration confirmation page with confetti
- ✅ Responsive design for mobile
- ✅ Shared database via Supabase

---

## 🗺️ AI Route Generation
The AI module generates surprise cycling routes around TalTech Tallinn based on participant level (Beginner / Intermediate / Advanced) and ride duration (30, 60, 90 min). Each route includes estimated distance and calories.

---

## 📊 BI Dashboard
Real-time analytics showing:
- Total participants & spots remaining
- Average Strava score
- Participants by level (chart)
- Bike rental vs own bike (chart)
- Strava score distribution (chart)
- Weight distribution (chart)

---

## 🔐 Admin Panel
Password protected panel for organizers to:
- View all registered participants
- Delete individual participants
- Reset all registrations

---

## 📄 Documentation
Full project documentation available in `/docs` folder:
- Project Charter
- SMART Objectives
- User Stories
- Integrated Project Plan

---

## 🚁 Event Details
- **Date:** June 4, 2026 | 18:00 - 20:00
- **Location:** TalTech, Tallinn, Estonia
- **Concept:** Follow the drone — destination is a surprise!

