'''
Create a function that takes two parameters of type int . The function should do the following:
Check if all the variables are negative . Else print "The numbers should be negative"
Check that the first parameter is smaller than the second parameter .
Using a loop Print all the numbers bettween the smaller int up to the bigger int .
'''


def ascending(first_number: int, second_number: int) -> None:
    if first_number and second_number < 0:
        if first_number < second_number:
            while second_number > first_number:
                print(first_number)
                first_number += 1
        else: 
            print("The first number is greater than second number")
    else:
        print("The numbers should be negative")


# Note: Ask the user for the 2 numbers. (use input)
first_input: int = int(input('Insert First Number: '))
second_input: int = int(input('Insert second Number: '))
ascending(first_input, second_input)
