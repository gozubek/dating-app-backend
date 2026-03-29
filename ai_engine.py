from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_ai_match_text(user1, user2, astro_data):

    prompt = f"""
    Analyze compatibility:

    User1:
    Sun: {astro_data['u1_sun']}
    Moon: {astro_data['u1_moon']}
    Venus: {astro_data['u1_venus']}

    User2:
    Sun: {astro_data['u2_sun']}
    Moon: {astro_data['u2_moon']}
    Venus: {astro_data['u2_venus']}

    Energy: {astro_data['energy']}

    Give:
    - compatibility insight
    - emotional dynamic
    - should they meet now?

    Max 3 sentences.
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content