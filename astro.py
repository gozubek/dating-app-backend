import swisseph as swe

# Zodiac list
SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer",
    "Leo", "Virgo", "Libra", "Scorpio",
    "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

# --- DEGREE → SIGN ---
def get_sign(degree):
    index = int(degree / 30)
    return SIGNS[index % 12]


# --- CHART CALCULATION ---
def get_chart(*args, **kwargs):
    return {"sun": 0, "moon": 0, "venus": 0}

def synastry_score(c1, c2):
    return 50

def get_sign(degree):
    return "Aries"


# --- ANGLE DIFFERENCE ---
def angle_diff(a, b):
    return min(abs(a - b), 360 - abs(a - b))


# --- SYNASTRY SCORE ---
def synastry_score(c1, c2):
    score = 0

    # Sun compatibility
    if angle_diff(c1["sun"], c2["sun"]) < 15:
        score += 30

    # Moon compatibility
    if angle_diff(c1["moon"], c2["moon"]) < 15:
        score += 30

    # Venus compatibility
    if angle_diff(c1["venus"], c2["venus"]) < 15:
        score += 40

    return score