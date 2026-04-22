def letter_grade(score):
    if not isinstance(score, (int, float)):
        raise TypeError ("Score must be number")

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def is_passing(score):
    if not isinstance(score, (int, float)):
        raise TypeError ("Score must be number")
    return score >= 60

def average(scores):
    if not isinstance(scores, list):
        raise TypeError("score must be list")
    if len(scores)== 0:
        raise ValueError("scores list cannot be empty")
    if not all(isinstance(s, (int,float))for s in scores):
        raise TypeError("all scores must be numbers")
    return round(sum(scores) / len(scores), 2)

def curved_score(score, bonus):
        if bonus < 0:
    raise ValueError("BONUS CANNOT BE NEGATIVE")
    return min(score + bonus, 100)
 