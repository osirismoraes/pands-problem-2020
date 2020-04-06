#This program will calculate a persons BMI using figures provided
#The inputs are the person's height in centimetres and weight in kilograms.
#The output is their weight divided by their height in metres squared.

weight = float(input("Enter your weight in KG; "))
height = float(input("Enter your height in meters; "))

heightsquared = (height * height)
bmi = weight / heightsquared

bmi2 = (round(bmi, 2))

print("Your BMI is", bmi2, "based on the figures you have provided")

