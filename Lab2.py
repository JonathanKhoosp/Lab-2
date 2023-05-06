print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    print("BMI = " + str(bmi))
    if bmi < 18.5:
        return -1  # Under weight
    elif bmi >= 18.5 and bmi < 25:
        return 0   # Normal weight
    else:
        return 1   # Over weight

# Get user input for height and weight
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))

# Call the calculate_bmi function with user input
bmi_classification = calculate_bmi(height, weight)

# Print the calculated BMI classification
if bmi_classification == -1:
    print("Under weight")
elif bmi_classification == 0:
    print("Normal weight")
else:
    print("Over weight")