print("-----------------------------------------------------------------------------")
print("Welcome to the BMI Calculator!")
print("-----------------------------------------------------------------------------")

try:
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    bmi = round(weight / (height ** 2), 2)

    print(f"Your BMI is {bmi}")

    if bmi < 18.5:
        print("Health Status: Underweight")
        print("Recommendation: You may need to gain some weight. Consider consulting a doctor or a nutritionist for a healthy diet plan.")
    elif bmi >= 18.5 and bmi < 24.9:
        print("Health Status: Normal weight")
        print("Recommendation: Great job! Maintain your healthy lifestyle with a balanced diet and regular exercise.")
    elif bmi >= 25 and bmi < 29.9:
        print("Health Status: Overweight")
        print("Recommendation: Consider adopting a more active lifestyle and a balanced diet. Small changes can make a big difference.")
    else:
        print("Health Status: Obesity")
        print("Recommendation: It is advisable to consult a healthcare professional to discuss a plan for weight management.")

    print("-----------------------------------------------------------------------------")
except ValueError:
    print("Invalid input. Please enter valid numeric values for weight and height.")