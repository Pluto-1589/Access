def get_bmi_category(height, weight):

    if height < 0:
        return "N/A"
    elif weight < 0:
        return "N/A"
    elif height and weight < 0:
        return "N/A"

    bmi = weight / (height**2)

    if bmi <= 18.5:
        return f"BMI: {bmi:.2f}, Category: Underweight"
    elif bmi <= 25:
        return f"BMI: {bmi:.2f}, Category: Normal weight"
    elif bmi <= 30:
        return f"BMI: {bmi:.2f}, Category: Pre-obesity"
    elif bmi > 30 and bmi <= 35:
        return f"BMI: {bmi:.2f}, Category: Obesity class I"
    elif bmi > 35 and bmi <= 40:
        return f"BMI: {bmi:.2f}, Category: Obesity class II"
    elif bmi > 40:
        return f"BMI: {bmi:.2f}, Category: Obesity class III"
    else:
        return "N/A"


print(get_bmi_category(1.8, 50))
