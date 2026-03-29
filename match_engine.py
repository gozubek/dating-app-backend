from astro import get_chart, synastry_score, get_sign

def find_best_match(current_user, users):

    best_match = None
    best_score = 0
    best_chart = None

    chart1 = get_chart(
        current_user.birth_year,
        current_user.birth_month,
        current_user.birth_day,
        current_user.birth_hour,
        current_user.birth_minute,
        current_user.timezone_offset
    )

    for user in users:
        if user == current_user:
            continue

        chart2 = get_chart(
            user.birth_year,
            user.birth_month,
            user.birth_day,
            user.birth_hour,
            user.birth_minute,
            user.timezone_offset
        )

        score = synastry_score(chart1, chart2)

        if score > best_score:
            best_score = score
            best_match = user
            best_chart = chart2

    if not best_match:
        return None

    return best_match, best_score, chart1, best_chart