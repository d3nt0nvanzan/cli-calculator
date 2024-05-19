#Imports Random Library and sys library
import random
import sys

restaurant = []#Starts with an empty list

choice = input('Enter restaurant: ')
restaurant.append(choice) #Has a user enter a restaurant name and appends it to the list
while choice != '0': #As long as the user doesn't enter zero it has them enter another restaurant
    choice = input('Enter restaurant:')
    restaurant.append(choice) #Appends restaurant to list while the choice is not zero
    newRestaurant = random.choice(restaurant) #The chosen restaurant is chosen at random and named new restaurant
    if choice == '0': #if the user enters zero the randomly chosen restaurant is printed and program is exited
        print(newRestaurant)
        sys.exit()
