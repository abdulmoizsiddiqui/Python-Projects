# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight/height**2
print(round(bmi,2))


if bmi <= 18.5:
  print("You are underweight")
elif bmi <= 25:
  print("You have a normal weight ")
elif bmi <= 30:
  print("You are overweight ")
elif bmi <= 35:
  print("You are obese")
else:
  print("Alert! Clinically Obese!")
  
