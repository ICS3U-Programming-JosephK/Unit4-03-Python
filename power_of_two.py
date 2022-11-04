#!/usr/bin/env python3

# Created by: Joseph Kwon
# Created on: November 3
# This program gets the user's input and outputs a
# #list if numbers up to the user's number to a power of 2


def main():

    # Tries to get the user's number as an integer.
    try:
        user_number = int(input("Enter a positive integer: "))

    # Exception thrown if the user did not enter a number
    except ValueError:
        input("You must enter a positive integer. Please try again.")

    # Restarts the program if the user entered a negative number
    if user_number < 0:
        print("You must enter a positive integer. Please try again.")

    else:

        # Initializing counter variable
        counter = 0

        # Code executed continually until user_number is equal to counter
        for counter in range(user_number + 1):
            power_of_two = counter**2
            print("{}^2 = {}".format(counter, power_of_two))


if __name__ == "__main__":
    main()
