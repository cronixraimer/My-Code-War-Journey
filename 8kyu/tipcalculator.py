import math

def calculate_tip(amount, rating):
    lower_case_rating = rating.lower()

    if lower_case_rating == 'terrible':
        return 0
    elif lower_case_rating == 'poor':
        return math.ceil(amount * 0.05)

    elif lower_case_rating == 'good':
        return math.ceil(amount * 0.1)

    elif lower_case_rating == 'great':
        return math.ceil(amount * 0.15)

    elif lower_case_rating == 'excellent':
        return math.ceil(amount * 0.2)

    else:
        return 'Rating not recognised'

result = calculate_tip(107.65, "Great")
print(result)
