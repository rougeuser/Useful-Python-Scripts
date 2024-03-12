import random

def roll_dice(sides):
    return random.randint(1, sides)

if __name__ == "__main__":
    sides = int(input("Enter the number of sides on the dice: "))
    print("Rolling the dice...", roll_dice(sides))
