def generate_astro_text(sun, moon, venus):

    personality = get_personality(sun)
    emotions = get_emotions(moon)
    love_style = get_love_style(venus)

    return {
        "personality": personality,
        "emotions": emotions,
        "love_style": love_style
    }


# --- PERSONALITY ---
def get_personality(sign):
    data = {
        "Aries": "Bold, energetic, and driven by action.",
        "Taurus": "Stable, loyal, and values comfort.",
        "Gemini": "Curious, communicative, and adaptable.",
        "Cancer": "Emotional, protective, and intuitive.",
        "Leo": "Confident, expressive, and loves attention.",
        "Virgo": "Analytical, practical, and detail-oriented.",
        "Libra": "Balanced, social, and harmony-seeking.",
        "Scorpio": "Intense, mysterious, and passionate.",
        "Sagittarius": "Adventurous, free-spirited, and optimistic.",
        "Capricorn": "Disciplined, ambitious, and responsible.",
        "Aquarius": "Independent, innovative, and unconventional.",
        "Pisces": "Dreamy, empathetic, and creative."
    }
    return data.get(sign, "Unique personality.")


# --- EMOTIONS ---
def get_emotions(sign):
    data = {
        "Aries": "React quickly and intensely.",
        "Taurus": "Emotionally steady and calm.",
        "Gemini": "Emotionally flexible and expressive.",
        "Cancer": "Deeply sensitive and nurturing.",
        "Leo": "Warm-hearted and expressive.",
        "Virgo": "Reserved and thoughtful.",
        "Libra": "Seeks emotional balance.",
        "Scorpio": "Deep and intense emotions.",
        "Sagittarius": "Light and freedom-loving.",
        "Capricorn": "Controlled and composed.",
        "Aquarius": "Detached but caring.",
        "Pisces": "Highly empathetic and emotional."
    }
    return data.get(sign, "Complex emotional nature.")


# --- LOVE STYLE ---
def get_love_style(sign):
    data = {
        "Aries": "Passionate and fast-moving in love.",
        "Taurus": "Loyal and committed partner.",
        "Gemini": "Playful and communicative.",
        "Cancer": "Caring and deeply attached.",
        "Leo": "Romantic and expressive.",
        "Virgo": "Shows love through actions.",
        "Libra": "Romantic and harmony-focused.",
        "Scorpio": "Intense and all-or-nothing.",
        "Sagittarius": "Needs freedom and excitement.",
        "Capricorn": "Serious and long-term oriented.",
        "Aquarius": "Unconventional and independent.",
        "Pisces": "Romantic and dreamy."
    }
    return data.get(sign, "Unique love expression.")