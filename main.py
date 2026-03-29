from fastapi import FastAPI
import random

from models import User
from database import users_db
from match_engine import find_best_match

from astro import get_sign
from astro_text import generate_astro_text
from ai_engine import generate_ai_match_text

app = FastAPI()

# --- CREATE USER ---
@app.post("/create_user")
def create_user(user: User):
    users_db.append(user)
    return {"message": "User added", "total_users": len(users_db)}

# --- MATCH ---
@app.get("/match/{index}")
def match_user(index: int):

    if index >= len(users_db):
        return {"error": "User not found"}

    current = users_db[index]

    result = find_best_match(current, users_db)

    if not result:
        return {"message": "No match found"}

    best_match, best_score, chart1, chart2 = result

    # --- SIGN ---
    sun1 = get_sign(chart1["sun"])
    moon1 = get_sign(chart1["moon"])
    venus1 = get_sign(chart1["venus"])

    sun2 = get_sign(chart2["sun"])
    moon2 = get_sign(chart2["moon"])
    venus2 = get_sign(chart2["venus"])

    # --- ASTRO TEXT ---
    astro_text = generate_astro_text(sun1, moon1, venus1)

    # --- ENERGY ---
    energy = random.choice(["High", "Neutral", "Low"])

    # --- AI ---
    astro_data = {
        "u1_sun": sun1,
        "u1_moon": moon1,
        "u1_venus": venus1,
        "u2_sun": sun2,
        "u2_moon": moon2,
        "u2_venus": venus2,
        "energy": energy
    }

    ai_text = generate_ai_match_text(current, best_match, astro_data)

    return {
        "match": best_match.name,
        "astro_score": best_score,
        "energy": energy,
        "astro_text": astro_text,
        "ai_insight": ai_text
    }