# Body Mass Index(BMI) Calculator
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")

#BMI: int = round(float(weight) / float(height) ** 2)
# print("Your Body Mass Index(BMI) is " + str(round(BMI)) + "kg/m²")

BMI = float(weight) // float(height) ** 2
print("Your Body Mass Index(BMI) is " + str(BMI) + "kg/m²")n

if BMI <= 18.5:
    print(f"Your BMI is {BMI}kg/m², you are underweight.")
elif BMI <= 25:
    print(f"Your BMI is {BMI}kg/m², you have a normal weight.")
elif BMI <= 30:
    print(f"Your BMI is {BMI}kg/m², you are overweight.")
elif BMI <= 35:
    print(f"Your BMI is {BMI}kg/m², you are obese.")
else:
    print(f"Your BMI is {BMI}kg/m², you are clinically obese.")
