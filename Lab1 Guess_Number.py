# Yunshu Zhao and Etienne Asselin
# 2015 Fall Term
# University of Alberta

import random
#Generate a random number
v_num = random.randint(1,10)
#Display instructions for player
print("I am thinking of a number between 1 and 10")
#Prompt player
v_guess = input("What is the number?")
#Display results
print("The number was ",v_num)
print("You guessed ",v_guess)