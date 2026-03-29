# astro.py

def get_chart(year, month, day, hour=0, minute=0, timezone_offset=0):
    # Basit hesap (demo)
    seed = (year + month + day + hour + minute) % 360

    return {
        "sun": seed % 360,
        "moon": (seed + 120) % 360,
        "venus": (seed + 240) % 360
    }


def get_sign(degree):
    SIGNS = [
        "Aries", "Taurus", "Gemini", "Cancer",
        "Leo", "Virgo", "Libra", "Scorpio",
        "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]

    return SIGNS[int(degree / 30) % 12]


def angle_diff(a, b):
    return min(abs(a - b), 360 - abs(a - b))


def synastry_score(c1, c2):
    score = 0

    if angle_diff(c1["sun"], c2["sun"]) < 30:
        score += 30

    if angle_diff(c1["moon"], c2["moon"]) < 30:
        score += 30

    if angle_diff(c1["venus"], c2["venus"]) < 30:
        score += 40

    return score