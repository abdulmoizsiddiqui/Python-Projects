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

love_score = str(TRUE) + str(LOVE)
love_score_int = int(love_score)
print("Love Score = " + love_score )

if love_score_int < 10 or love_score_int > 90:
  print(f"Your Love Score is {love_score}. You go together like Coke and Mentos!")
elif love_score_int < 50 and love_score_int > 40:
  print(f"Your Love Score is {love_score}. You are alright together.")
else:
  print(f"Your score is {love_score}.")