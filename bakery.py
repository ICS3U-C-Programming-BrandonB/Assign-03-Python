#!/usr/bin/env python3

# Created By: Brandon
# Date: November 7th, 2025
# This program calculates the total cost of croissants ordered at a bakery

import constants


def main():

    # gets number of croissants from user
    item_count = input(
        "Welcome to Brandon's Bakery! How many croissants would you like to order? "
    )

    # Checking if the user entered an integer correctly
    try:
        # casting variable to an integer
        item_count = int(item_count)
        print("You entered an Integer!")

        # calculate subtotal, tax, and total
        subtotal = item_count * constants.CROISSANT_PRICE
        tax = subtotal * constants.HST
        total = subtotal + tax

        # determine whether or not the user has to pay tax
        if item_count < 6:
            print(
                "You need to order 6 or more croissants to not pay tax, your total is ${:.2f}".format(
                    total
                )
            )
        else:
            print(
                "You ordered more than 6 croissants, you don't have to pay tax! Your Total is: ${:.2f}".format(
                    subtotal
                )
            )
    # exception handling, making sure user enters an integer
    except ValueError:
        print("Please Enter a Valid Integer")


# outputs the function
if __name__ == "__main__":
    main()
