exit_keyword= "exit"
user_input= input("Choose what function you want me to perform:")

if user_input == '1':
    print("Hello:")
elif user_input == '2':
    print("This is second user_input")
elif user_input == '3':
    print("This is the third user_input")
elif user_input == '4':
    print("This the 4th user_input")
elif user_input == '5':
    print("This is 5th user_input")
else:
    print("You chose an invalid user_input")

while user_input != exit_keyword:
    print("You have sucesfully exited the  program!")   
#