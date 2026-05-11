import random

# Waypoints around TalTech Tallinn
WAYPOINTS = {
    "easy": [
        {"name": "TalTech Main Building", "lat": 59.3956, "lng": 24.6674},
        {"name": "Ülemiste Lake", "lat": 59.4066, "lng": 24.7452},
        {"name": "Kadriorg Park", "lat": 59.4372, "lng": 24.7916},
        {"name": "Pirita Beach", "lat": 59.4661, "lng": 24.8329},
        {"name": "Botanical Garden", "lat": 59.4425, "lng": 24.8021},
    ],
    "intermediate": [
        {"name": "TalTech Main Building", "lat": 59.3956, "lng": 24.6674},
        {"name": "Tallinn Old Town", "lat": 59.4370, "lng": 24.7454},
        {"name": "Pirita Promenade", "lat": 59.4661, "lng": 24.8329},
        {"name": "Maarjamäe Palace", "lat": 59.4533, "lng": 24.8012},
        {"name": "Song Festival Grounds", "lat": 59.4436, "lng": 24.7982},
        {"name": "Kadriorg Palace", "lat": 59.4372, "lng": 24.7916},
    ],
    "advanced": [
        {"name": "TalTech Main Building", "lat": 59.3956, "lng": 24.6674},
        {"name": "Tallinn Old Town", "lat": 59.4370, "lng": 24.7454},
        {"name": "Pirita Beach", "lat": 59.4661, "lng": 24.8329},
        {"name": "Rocca al Mare", "lat": 59.4321, "lng": 24.6512},
        {"name": "Stroomi Beach", "lat": 59.4512, "lng": 24.6821},
        {"name": "Kopli Peninsula", "lat": 59.4612, "lng": 24.6921},
        {"name": "Kalamaja", "lat": 59.4456, "lng": 24.7123},
        {"name": "Telliskivi", "lat": 59.4401, "lng": 24.7234},
    ]
}

ROUTE_NAMES = [
    "The Silent Forest Path",
    "The Coastal Wind Route",
    "The Historic Trail",
    "The Sunset Rider",
    "The Urban Explorer",
    "The Hidden Gems Tour",
    "The Baltic Breeze",
    "The Mystery Loop"
]

def generate_route(level: str = "intermediate", duration_minutes: int = 60):
    level_key = level.lower()
    if level_key not in WAYPOINTS:
        level_key = "intermediate"

    waypoints = WAYPOINTS[level_key].copy()
    random.shuffle(waypoints[1:])  # Keep TalTech as start

    # Select waypoints based on duration
    if duration_minutes <= 30:
        selected = waypoints[:3]
    elif duration_minutes <= 60:
        selected = waypoints[:4]
    else:
        selected = waypoints[:6]

    # Always end at TalTech
    selected.append(WAYPOINTS[level_key][0])

    route_name = random.choice(ROUTE_NAMES)
    estimated_distance = round(len(selected) * 2.5 + random.uniform(0.5, 2.0), 1)
    calories = round(estimated_distance * 40 + random.uniform(10, 50))

    return {
        "name": route_name,
        "level": level,
        "duration_minutes": duration_minutes,
        "estimated_distance_km": estimated_distance,
        "estimated_calories": calories,
        "waypoints": selected,
        "start": selected[0]["name"],
        "end": selected[-1]["name"]
    }

def get_surprise_routes(level: str = "intermediate"):
    routes = []
    for duration in [30, 60, 90]:
        route = generate_route(level, duration)
        routes.append(route)
    return routes