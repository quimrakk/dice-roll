from random import randrange
import os

def diceRoll(sides, numOfDie):
    if numOfDie > 1:
        for i in range(1, numOfDie + 1):
            print(f"Die #{i}: {randrange(1, sides)}")
    else:
        print(f'\nDie #1: {randrange(1, 7)}')

    print("Do you want to roll again? (y/n)")
    again = input("")
    if again == 'y' or again == 'ye' or again == 'yes':
        pre()
    else:
        quit()

def pre():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Roll Dice")
    while True:
        try:
            print("\nPlease enter the amount of die you want to roll: ")
            num = int(input(""))
        except ValueError:
            print("You must enter a number")
        else:
            break

    while True:
        try:
            print("\nPlease enter the amount of sides each die will have: ")
            sides = int(input(""))
        except ValueError:
            print("You must enter a number")
        else:
            break

    diceRoll(sides, num)


if __name__ == "__main__":
    pre()
