choice= input("Choose what function you want me to perform:")
exit= False

if choice == '1':
    print("Hello:")
elif choice == '2':
    print("This is second choice")
elif choice == '3':
    print("This is the third choice")
elif choice == '4':
    print("This the 4th choice")
elif choice == '5':
    print("This is 5th choice")
else:
    print("You chose an invalid choice")

while choice != 'exit':
    print("Do you want to perform another task?")
    choice= input("Choose what function you want me to perform:")
