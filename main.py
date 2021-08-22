# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height**2)
print(bmi)

if bmi <= 18:
  print(f'Your BMI is {bmi}, you are underweight.')
elif bmi > 19 and bmi < 25:
  print(f'Your BMI is {bmi}, you are a normal weight.')
elif bmi > 25 and bmi < 30:
  print(f'Your BMI is {bmi}, you are slightly overweight.')
elif bmi > 30 and bmi < 35:
  print(f'Your BMI is {bmi}, you are obese.')
else:
  print(f'Your BMI is above 35, you are clinically obese.')



