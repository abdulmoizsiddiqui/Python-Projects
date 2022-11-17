starting_position = int(input('Please enter the starting range: \n'))
ending_position = int(input('Please enter the ending range: \n'))

if ending_position < starting_position:

    # swapping the values
    swap = starting_position
    starting_position = ending_position
    ending_position = swap

    for i in range (starting_position, ending_position + 1):
        if i % 2 == 0:
            print(i)
elif ending_position > starting_position:
       for i in range (starting_position, ending_position + 1):
        if i % 2 == 0:
            print(i)