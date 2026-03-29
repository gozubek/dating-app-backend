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
def get_chart(year, month, day, hour=0, minute=0, timezone_offset=0):

    # Convert local time → UTC
    utc_hour = hour - timezone_offset

    # Add minute
    time_decimal = utc_hour + (minute / 60)

    # Julian day
    jd = swe.julday(year, month, day, time_decimal)

    # Planet positions
    sun = swe.calc_ut(jd, swe.SUN)[0][0]
    moon = swe.calc_ut(jd, swe.MOON)[0][0]
    venus = swe.calc_ut(jd, swe.VENUS)[0][0]

    return {
        "sun": sun,
        "moon": moon,
        "venus": venus
    }


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