# Write a program to determine the BMI Category based on user input.

height=float(input("Enter the height in meters : "))
weight=float(input("enter the weight in kilograms : "))

# Uisng the BMI Formula

bmm = weight/(height)*2
bmi = int(bmm)

# applying the main logic

if bmi >= 30:
    print("Your BMI is :",bmi, "Obesity")
elif 25 <= bmi < 30:
    print("Your BMI is :",bmi, "Overweight")
elif 18.5 <= bmi < 25:
    print("Your BMI is :",bmi, "Normal")
else:
    print("Your BMI is :",bmi, "Underweight")
    
  ## Succesfully calculated the BMI using the given logic
