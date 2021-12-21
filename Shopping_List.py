#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Write a program to prompt the user to enter a number of items and their prices.
# The program should then sort the input from highest to lowest price and
# output the sorted data showing the item and the price.

# Here comes your imports

# Here comes your (few) global variables

# Here comes your function definitions

def main():
    print("Welcome To Shopping List!")
    numItems = input("How many do you want?")
    myTup  = ()
    myList = []

    for x in range(int(numItems)):
        itemName  = input("Enter item name: ")
        itemPrice = input("Enter item price:")
        myTup     = (itemPrice, itemName)
        myList.append(myTup)

    myList.sort()
    print(myList)

if __name__ == "__main__":
        main()