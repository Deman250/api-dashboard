#API project
print("=== API Dashboard ====")
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
        "member_count": 6
    }

def fetch_active_skills():
    return {
        "week": "2024-W47",
        "skills": [
            {"name": "welding",       "instructor": "Patrick Njiru", "enrolled": 8},
            {"name": "tiling",        "instructor": "James Omondi",  "enrolled": 12},
            {"name": "copywriting",   "instructor": "Sandra Weru",   "enrolled": 15},
            {"name": "phone repair",  "instructor": "Kevin Mwangi",  "enrolled": 10},
            {"name": "beekeeping",    "instructor": "Grace Achieng", "enrolled": 6},
        ]
    }

# Preview
members = fetch_members()
weekly = fetch_weekly_summary()
skills = fetch_active_skills()

print(f"Members endpoint: {len(members)} records")
print(f"Weekly endpoint:  {len(weekly['daily_totals'])} days of data")
print(f"Skills endpoint:  {len(skills['skills'])} active skills")

#Step 2: Processing each endpoint
print("=== Processing members... ====")
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
        "top": max(members, key=lambda m: m["steps"])["name"]
    }

def process_weekly(weekly):
    totals = weekly["daily_totals"]
    days = weekly["days"]
    best_idx = totals.index(max(totals))
    return {
        "best_day": days[best_idx],
        "best_total": max(totals),
        "weekly_avg": round(sum(totals) / len(totals)),
        "total_steps": sum(totals)
    }

def process_skills(skills_data):
    skills = skills_data["skills"]
    total_enrolled = sum(s["enrolled"] for s in skills)
    most_popular = max(skills, key=lambda s: s["enrolled"])
    return {
        "active_count": len(skills),
        "total_enrolled": total_enrolled,
        "most_popular": most_popular["name"],
        "top_enrollment": most_popular["enrolled"]
    }

# Run all three
raw_members = [
    {"name": "James Omondi",  "steps": 9200,  "protocol": "OMAD", "sleep": 7.5, "cold_shower": True},
    {"name": "Sandra Weru",   "steps": 10500, "protocol": "2MAD", "sleep": 8.0, "cold_shower": True},
    {"name": "Patrick Njiru", "steps": 8100,  "protocol": "OMAD", "sleep": 6.5, "cold_shower": False},
    {"name": "Grace Achieng", "steps": 11000, "protocol": "OMAD", "sleep": 7.0, "cold_shower": True},
    {"name": "Brian Kamau",   "steps": 7400,  "protocol": "2MAD", "sleep": 9.0, "cold_shower": True},
    {"name": "Kevin Mwangi",  "steps": 10800, "protocol": "OMAD", "sleep": 7.5, "cold_shower": True},
]
raw_weekly = {"week": "2024-W47", "daily_totals": [54200, 62000, 58400, 71000, 49600, 68000, 65200], "days": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"], "member_count": 6}
raw_skills = {"week": "2024-W47", "skills": [{"name": "welding","instructor": "Patrick Njiru","enrolled": 8},{"name": "tiling","instructor": "James Omondi","enrolled": 12},{"name": "copywriting","instructor": "Sandra Weru","enrolled": 15},{"name": "phone repair","instructor": "Kevin Mwangi","enrolled": 10},{"name": "beekeeping","instructor": "Grace Achieng","enrolled": 6}]}

member_stats = process_members(raw_members)
weekly_stats = process_weekly(raw_weekly)
skill_stats = process_skills(raw_skills)

print("Member stats:", member_stats)
print("Weekly stats:", weekly_stats)
print("Skill stats: ", skill_stats)

#Combined Dashboard
print("=== Full Dashboard ====")
import json

import urllib

import urllib

# --- Data (simulated API responses) ---
raw_members = [
    {"name": "James Omondi",  "steps": 9200,  "protocol": "OMAD", "sleep": 7.5, "cold_shower": True},
    {"name": "Sandra Weru",   "steps": 10500, "protocol": "2MAD", "sleep": 8.0, "cold_shower": True},
    {"name": "Patrick Njiru", "steps": 8100,  "protocol": "OMAD", "sleep": 6.5, "cold_shower": False},
    {"name": "Grace Achieng", "steps": 11000, "protocol": "OMAD", "sleep": 7.0, "cold_shower": True},
    {"name": "Brian Kamau",   "steps": 7400,  "protocol": "2MAD", "sleep": 9.0, "cold_shower": True},
    {"name": "Kevin Mwangi",  "steps": 10800, "protocol": "OMAD", "sleep": 7.5, "cold_shower": True},
]
daily_steps = [54200, 62000, 58400, 71000, 49600, 68000, 65200]
day_names   = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
skills_list = [
    {"name": "welding",      "enrolled": 8},
    {"name": "tiling",       "enrolled": 12},
    {"name": "copywriting",  "enrolled": 15},
    {"name": "phone repair", "enrolled": 10},
    {"name": "beekeeping",   "enrolled": 6},
]

# --- Process ---
STEP_GOAL = 10000
goal_met = [m for m in raw_members if m["steps"] >= STEP_GOAL]
avg_steps = round(sum(m["steps"] for m in raw_members) / len(raw_members))
showers   = sum(1 for m in raw_members if m["cold_shower"])
best_day  = day_names[daily_steps.index(max(daily_steps))]
top_skill = max(skills_list, key=lambda s: s["enrolled"])

# --- Output ---
W = 52
print("=" * W)
print(f"  SMP COMMAND CENTRE DASHBOARD  |  Week 2024-W47")
print("=" * W)

print(f"\n  SECTION 1: MEMBER PERFORMANCE")
print(f"  {'Total members:':<28} {len(raw_members)}")
print(f"  {'Hit {STEP_GOAL:,} step goal:':}")
print(f"  Hit {STEP_GOAL:,} step goal:          {len(goal_met)}/{len(raw_members)}")
print(f"  {'Average steps:':<28} {avg_steps:,}")
print(f"  {'Cold showers today:':<28} {showers}/{len(raw_members)}")
print(f"  Goal hitters: {', '.join(m['name'] for m in goal_met)}")

print(f"\n  SECTION 2: WEEKLY STEPS")
for day, total in zip(day_names, daily_steps):
    bar = "#" * (total // 5000)
    print(f"  {day:4} {total:>7,}  {bar}")
print(f"  Best day: {best_day} ({max(daily_steps):,} total steps)")
print(f"  Week avg: {round(sum(daily_steps)/len(daily_steps)):,} steps/day")

print(f"\n  SECTION 3: ACTIVE SMP SKILLS")
for s in sorted(skills_list, key=lambda x: -x["enrolled"]):
    print(f"  {s['name']:15} {s['enrolled']} enrolled")
print(f"  Most popular: {top_skill['name']} ({top_skill['enrolled']} enrolled)")

print(f"\n{'=' * W}")

# JSON export
export = {
    "week": "2024-W47",
    "members": {"total": len(raw_members), "goal_met": len(goal_met), "avg_steps": avg_steps},
    "weekly": {"best_day": best_day, "total_steps": sum(daily_steps)},
    "skills": {"active": len(skills_list), "most_popular": top_skill["name"]}
}
print("\nJSON export:")
print(json.dumps(export, indent=2))

#Week 5 EXCERCISES
print("=== PARSING JSON ===")
import json
# Parse this nested JSON and print the author and title
response = '{"book": {"title": "Clean Code", "author": "Robert Martin", "year": 2008}}'
data = json.loads(response)
book = data["book"]
print(f"Title: {book['title']}")
print(f"Author: {book['author']}")

print(" ==== CHALLENGE ====")
import urllib.request, json
# Fetch a joke from a public API and print it
url = "https://official-joke-api.appspot.com/random_joke"
try:
    with urllib.request.urlopen(url, timeout=5) as r:
        joke = json.loads(r.read())
    print(joke['setup'])
    print(joke['punchline'])
except Exception as e:
    print(f"Could not fetch joke: {e}")

print(" ==== TRADE APPLICATION - WELDING JOB QUOTE ====")
import json

# Simulated API response from a steel supplier
response_text = '''
{
    "supplier": "Nairobi Steel Ltd",
    "date": "2026-07-27",
    "prices": {
        "mild_steel_sheet": 4500,
        "angle_iron": 2800,
        "square_tube": 3200
    },
    "currency": "KES",
    "unit": "per metre"
}
'''

data = json.loads(response_text)

print(f"Supplier: {data['supplier']}")
print(f"Date: {data['date']}")
print(f"\nSteel prices ({data['currency']} {data['unit']}):")
for item, price in data["prices"].items():
    print(f"  {item.replace('_', ' ').title()}: KES {price:,}")

# One steel door frame: 3 pieces of angle iron (2m each) + 1 mild steel sheet
angle_cost = data["prices"]["angle_iron"] * 2 * 3
sheet_cost = data["prices"]["mild_steel_sheet"]
frame_cost = angle_cost + sheet_cost

print(f"\nDoor frame quote:")
print(f"  Angle iron (3 x 2m): KES {angle_cost:,}")
print(f"  Mild steel sheet: KES {sheet_cost:,}")
print(f"  Total: KES {frame_cost:,}")

#Exercise 4
print(" ==== FARMING APPLICATION - CROP MARKET CHECKER ====")
import json

# Simulated crop market API response
response_text = '''
{
    "market": "Wakulima Market, Nairobi",
    "date": "2026-07-27",
    "prices_per_bag_kes": {
        "maize": 3800,
        "beans": 9200,
        "wheat": 5500,
        "sorghum": 3200
    },
    "bag_weight_kg": 90
}
'''

data = json.loads(response_text)

# Farmer's current stock in bags
stock = {"maize": 12, "beans": 5, "wheat": 8, "sorghum": 20}

print(f"Market: {data['market']}")
print(f"Date: {data['date']}\n")
print("Crop Valuation:")
print("-" * 40)

total_value = 0
for crop, bags in stock.items():
    price = data["prices_per_bag_kes"][crop]
    value = bags * price
    print(f"{crop.title()}: {bags} bags x KES {price:,} = KES {value:,}")
    total_value += value

print(f"\nTotal stock value: KES {total_value:,}")

#Week 5 Assignment
print("==== Code challenge - Social media API ====")

data = {
    "user": "Amerix",
    "followers": 1200000,
    "last_post": {
        "title": "Cold shower protocol",
        "likes": 4800
    }
}
print(f"Followers: {data['followers']:}")
print(f"Last post likes: {data['last_post']['likes']:}")
#code challenge 2
print("==== SUPPLIER PRICING API ====")
data = {
    "supplier": "Nairobi Steel Ltd",
    "prices": {
        "mild_steel_sheet": 4500,
        "angle_iron": 2800
    }
}
mild_steel_price = data["prices"]["mild_steel_sheet"]*3
angle_iron_price = data["prices"]["angle_iron"]*6
print(f"Supplier: {data['supplier']}")
print(f"Mild steel sheets (3): KES {mild_steel_price}")
print(f"Angle iron (6m): KES {angle_iron_price}")
Total = mild_steel_price + angle_iron_price
print(f"Total : KES {Total}")
#CODE 3
print("==== BOLT DRIVER EARNINGS ====")
data = {
    "driver": "Kamau Njoroge",
    "date": "2026-08-13",
    "trips": [
        {"route": "Westlands to CBD",     "fare_kes": 560},
        {"route": "CBD to South B",       "fare_kes": 420},
        {"route": "South B to Karen",     "fare_kes": 980},
        {"route": "Karen to Westlands",   "fare_kes": 720},
        {"route": "Westlands to Airport", "fare_kes": 740},
    ]
}
for t in data["trips"]:
    Earning_for_trips = sum(t["fare_kes"] for t in data["trips"])
print(f"Total trips: 5")
print(f"Total earned: KES {Earning_for_trips}")
print("Highest trip: South B to Karen | KES 980")