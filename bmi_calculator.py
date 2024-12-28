height = float(input("What is your height in Mt?\n"))
weight = int(input("What is your weight in KG?"))

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight / (height * height)

print(f"your BMI is {bmi}")

if bmi > 18.5 and bmi < 25:
    print ("Your BMI is normal, perfect!")
elif bmi > 25 and bmi < 30:
    print ("You are over weight")
elif bmi > 30:
    print ("You are in Obesity stage, reduce weight soon")
else:
    print("You are underweight! Eat healty and increase weight")
