# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = name1.lower()
name2 = name2.lower()



T= name1.count("t") + name2.count("t")
print(f"T occurs {T} times")
R= name1.count("r") + name2.count("r")
print(f"R occurs {R} times")
U= name1.count("u") + name2.count("u")
print(f"U occurs {U} times")
E= name1.count("e") + name2.count("e")
print(f"E occurs {E} times")
TRUE= T+R+U+E
print(f"Total: {TRUE}")


L= name1.count("l") + name2.count("l")
print(f"L occurs {L} times")
O= name1.count("o") + name2.count("o")
print(f"O occurs {O} times")
V= name1.count("v") + name2.count("v")
print(f"V occurs {V} times")
E= name1.count("e") + name2.count("e")
print(f"E occurs {E} times")
LOVE= L+O+V+E
print(f"Total: {LOVE}")

print("Love Score = " + str(TRUE) + str(LOVE))