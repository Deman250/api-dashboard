"""
api-dashboard — FastAPI service

Wraps the project's simulated data sources (member activity, weekly steps,
active skills, supplier pricing, Bolt driver earnings) as real HTTP
endpoints. Run locally with:

    uvicorn main:app --reload

Then visit http://127.0.0.1:8000/docs for interactive, click-to-test docs.
"""

from fastapi import FastAPI

app = FastAPI(
    title="api-dashboard",
    description="Multi-endpoint dashboard with simulated API-style data, grouped by protocol.",
    version="1.0.0",
)


# --- Data sources (simulated — same shape a real API would return) ---

def fetch_members():
    return [
        {"name": "James Omondi",  "steps": 9200,  "protocol": "OMAD", "sleep": 7.5, "cold_shower": True},
        {"name": "Sandra Weru",   "steps": 10500, "protocol": "2MAD", "sleep": 8.0, "cold_shower": True},
        {"name": "Patrick Njiru", "steps": 8100,  "protocol": "OMAD", "sleep": 6.5, "cold_shower": False},
        {"name": "Grace Achieng", "steps": 11000, "protocol": "OMAD", "sleep": 7.0, "cold_shower": True},
        {"name": "Brian Kamau",   "steps": 7400,  "protocol": "2MAD", "sleep": 9.0, "cold_shower": True},
        {"name": "Kevin Mwangi",  "steps": 10800, "protocol": "OMAD", "sleep": 7.5, "cold_shower": True},
    ]


def fetch_weekly_summary():
    return {
        "week": "2024-W47",
        "daily_totals": [54200, 62000, 58400, 71000, 49600, 68000, 65200],
        "days": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "member_count": 6,
    }


def fetch_active_skills():
    return {
        "week": "2024-W47",
        "skills": [
            {"name": "welding",      "instructor": "Patrick Njiru", "enrolled": 8},
            {"name": "tiling",       "instructor": "James Omondi",  "enrolled": 12},
            {"name": "copywriting",  "instructor": "Sandra Weru",   "enrolled": 15},
            {"name": "phone repair", "instructor": "Kevin Mwangi",  "enrolled": 10},
            {"name": "beekeeping",   "instructor": "Grace Achieng", "enrolled": 6},
        ],
    }


def fetch_steel_prices():
    return {
        "supplier": "Nairobi Steel Ltd",
        "prices": {"mild_steel_sheet": 4500, "angle_iron": 2800},
    }


def fetch_bolt_trips():
    return {
        "driver": "Kamau Njoroge",
        "date": "2026-08-13",
        "trips": [
            {"route": "Westlands to CBD",     "fare_kes": 560},
            {"route": "CBD to South B",       "fare_kes": 420},
            {"route": "South B to Karen",     "fare_kes": 980},
            {"route": "Karen to Westlands",   "fare_kes": 720},
            {"route": "Westlands to Airport", "fare_kes": 740},
        ],
    }


# --- Processing (unchanged from the original scripts) ---

def process_members(members, step_goal=10000):
    goal_met = [m for m in members if m["steps"] >= step_goal]
    avg_steps = round(sum(m["steps"] for m in members) / len(members))
    shower_count = sum(1 for m in members if m["cold_shower"])
    protocols = {}
    for m in members:
        p = m["protocol"]
        protocols[p] = protocols.get(p, 0) + 1
    return {
        "total": len(members),
        "goal_met": len(goal_met),
        "avg_steps": avg_steps,
        "cold_showers": shower_count,
        "protocols": protocols,
        "top": max(members, key=lambda m: m["steps"])["name"],
    }


def process_weekly(weekly):
    totals = weekly["daily_totals"]
    days = weekly["days"]
    best_idx = totals.index(max(totals))
    return {
        "best_day": days[best_idx],
        "best_total": max(totals),
        "weekly_avg": round(sum(totals) / len(totals)),
        "total_steps": sum(totals),
    }


def process_skills(skills_data):
    skills = skills_data["skills"]
    total_enrolled = sum(s["enrolled"] for s in skills)
    most_popular = max(skills, key=lambda s: s["enrolled"])
    return {
        "active_count": len(skills),
        "total_enrolled": total_enrolled,
        "most_popular": most_popular["name"],
        "top_enrollment": most_popular["enrolled"],
    }


# --- Routes ---

@app.get("/")
def root():
    return {
        "service": "api-dashboard",
        "endpoints": [
            "/members", "/members/stats",
            "/weekly-summary", "/weekly-summary/stats",
            "/skills", "/skills/stats",
            "/steel-quote", "/bolt-earnings",
        ],
    }


@app.get("/members")
def members():
    return fetch_members()


@app.get("/members/stats")
def members_stats():
    return process_members(fetch_members())


@app.get("/weekly-summary")
def weekly_summary():
    return fetch_weekly_summary()


@app.get("/weekly-summary/stats")
def weekly_summary_stats():
    return process_weekly(fetch_weekly_summary())


@app.get("/skills")
def skills():
    return fetch_active_skills()


@app.get("/skills/stats")
def skills_stats():
    return process_skills(fetch_active_skills())


@app.get("/steel-quote")
def steel_quote():
    """Door frame quote: 3 pieces of angle iron (2m each) + 1 mild steel sheet."""
    data = fetch_steel_prices()
    angle_cost = data["prices"]["angle_iron"] * 2 * 3
    sheet_cost = data["prices"]["mild_steel_sheet"]
    return {
        "supplier": data["supplier"],
        "angle_iron_cost_kes": angle_cost,
        "mild_steel_sheet_cost_kes": sheet_cost,
        "total_kes": angle_cost + sheet_cost,
    }


@app.get("/bolt-earnings")
def bolt_earnings():
    data = fetch_bolt_trips()
    total = sum(t["fare_kes"] for t in data["trips"])
    highest = max(data["trips"], key=lambda t: t["fare_kes"])
    return {
        "driver": data["driver"],
        "date": data["date"],
        "total_trips": len(data["trips"]),
        "total_earned_kes": total,
        "highest_trip": highest["route"],
        "highest_fare_kes": highest["fare_kes"],
    }
