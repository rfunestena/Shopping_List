#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Write a program to prompt the user to enter a number of items and their prices.
# The program should then sort the input from highest to lowest price and
# output the sorted data showing the item and the price.

# Here comes your imports
import json
# Here comes your (few) global variables
myList  = []
myShoppingList = []
myShoppingListFiltered = []

# Here comes your function definitions

def main():
    print("Welcome To Shopping List!")
    rangeList    = EnterIngredients()
    NewRangeList = SortIngredients(rangeList)
    OutpIngredients(NewRangeList)
    create_json()



def EnterIngredients():
    #Initialize variables
    numItems     = 0
    EndofList    = "Yes"
    while (EndofList != "no"):
        itemName     = input("Enter item name: ")
        itemCategory = input("Enter item Category: ")
        itemQuantity = int(input("Enter item Quantity: "))
        EndofList    = input("Do you want to add another item?:")
        myList       = [itemName, itemCategory, itemQuantity]
        myShoppingList.append(myList)
        numItems += 1
    return numItems


def SortIngredients(rangeList):
# Look through the list and add same items
# that user has introduced at different recipes
# set to zero one of the items once it has been added.
    #Initialize variables
    numItemsFinalList = 0
    for x in range(int(rangeList)):
        for i in range(int(rangeList)):
            if ((myShoppingList[x][0] == myShoppingList[i][0]) and (i != x)):
                myShoppingList[x][2] += myShoppingList[i][2]
                myShoppingList[i][2] = 0
                #print(myShoppingList[x])
# Remove cells that are set to zero
# And asign it to a new list                
    for z in range(int(rangeList)):
        if (myShoppingList[z][2] != 0):
            myShoppingListFiltered.append(myShoppingList[z])
            numItemsFinalList += 1
    return numItemsFinalList
        

def OutpIngredients(NewRangeList):
    print("Name, Category, Quantity")
    for x in range(int(NewRangeList)): 
        print(myShoppingListFiltered[x])

def create_json():
    with open('/home/raul/Documents/Raul/Sw_Dev/Shopping_List/Shopping_List.txt','w') as file:
        json.dump(myShoppingListFiltered, file)

if __name__ == "__main__":
        main()