print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")


def calculate_bmi(height, weight):
 print("Height = " + str(height))
 print("Weight = " + str(weight))
 bmi = weight / (height * height)
 print("BMI = " + str(bmi))


calculate_bmi(height=1.73, weight=57)
