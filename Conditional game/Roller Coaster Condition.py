print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is yor age? "))

if height >= 120:
    print("Can ride that Roller Coaster!")
    if age <12:
        bill = 5
        print(f"Child tickets are ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill}")
    elif age > 45 and age < 55:
        bill = 0
        print("The bill's on us! Enjoy your ride :)")
else:
    print("Cant ride Roller Coaster :(")