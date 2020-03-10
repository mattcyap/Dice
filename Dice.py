#  File: Dice.py
#  Description: Program that simulates rolling a dice multiple times and shows the results.
#  Student's Name: Matthew Yap
#  Student's UT EID: my5476
#  Course Name: CS 313E 
#  Unique Number: 51470
#
#  Date Created: 9/14/2017
#  Date Last Modified: 9/14/2017
import random

#   defines the variable for the dices
class Roll:

    def __init__(self, roll_one, roll_two):
        self.x = roll_one
        self.y = roll_two

    #   adds the result of the rolls together
    def add(self):
        return self.x + self.y

def main():
    #   seed value to make it easier to grade
    random.seed(1314)

    #   prompt the user for the amount of rolls
    number_of_rolls = eval(input("How many times do you want to roll the dice? "))

    #   sets up variables for the while loop and a list to hold the rolls
    count = 0
    hold_rolls = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #   loops to "roll" the dice and keeps track of the results
    while(count < number_of_rolls):

        #   uses the random function to simulate rolling dice
        dice_one = random.randint(1, 6)
        dice_two = random.randint(1, 6)

        #   uses the class to add the dice together
        use_class = Roll(dice_one, dice_two)

        #   increments the counter for the while loop
        count = count + 1

        #   uses the class function to add the dice
        total = use_class.add()

        #   logs the results into the list
        if total == 2:
            hold_rolls[0] = hold_rolls[0] + 1

        elif total == 3:
            hold_rolls[1] = hold_rolls[1] + 1

        elif total == 4:
            hold_rolls[2] = hold_rolls[2] + 1

        elif total == 5:
            hold_rolls[3] = hold_rolls[3] + 1

        elif total == 6:
            hold_rolls[4] = hold_rolls[4] + 1

        elif total == 7:
            hold_rolls[5] = hold_rolls[5] + 1
    
        elif total == 8:
            hold_rolls[6] = hold_rolls[6] + 1

        elif total == 9:
            hold_rolls[7] = hold_rolls[7] + 1

        elif total == 10:
            hold_rolls[8] = hold_rolls[8] + 1

        elif total == 11:
            hold_rolls[9] = hold_rolls[9] + 1

        elif total == 12:
            hold_rolls[10] = hold_rolls[10] + 1

    #   shows the results of the dice rolling
    print("Results:",hold_rolls)
    print()

    #   alters the results to the correct scale
    for i in range(len(hold_rolls)):
        while(hold_rolls[i] > 20):
            hold_rolls_one = hold_rolls[i] // 1
            hold_rolls[i] = hold_rolls[i] / 10

            if hold_rolls[i] >= (hold_rolls_one + 0.50):
                hold_rolls[i] = hold_rolls_one + 1

    #   counter variable to print the lines
    counter = 0

    #   variable to keep track of the max number of lines
    hold_lines = max(hold_rolls)

    #   while loop to print out the graph
    while max(hold_rolls) > counter:
        print("|",end="  ")
        for i in range(len(hold_rolls)):
            if hold_rolls[i] >= hold_lines:
                print("*",end="  ")
            else:
                print(" ",end="  ")
        print()
        hold_lines = hold_lines - 1
        counter = counter + 1
    print("+--+--+--+--+--+--+--+--+--+--+--+-")
    print("   2  3  4  5  6  7  8  9 10 11 12")

main()
        
