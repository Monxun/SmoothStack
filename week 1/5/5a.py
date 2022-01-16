
def bmi_score(weight, height):
    return weight / (height**2)

def bmi_analysis(score):
    if score < 18.5:
        return "under"
    elif score < 25:
        return "normal"
    elif score < 30:
        return "over"
    else:
        return "obese"

def bmi_calculator(people, str):
    results = []
    for _ in people:
        weight, height = str.split(' ')
        score = bmi_score(weight, height)
        result = bmi_analysis(score)
        results.append(result)
    return " ".join(results)
