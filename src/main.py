import sys
from Card import *
from Draws import *

def menu():
    print("What do you want to do?\n")
    print("1: Generate a Card\n2: Print the Card\n3: Exit\n\n")
    choice = input()
    return int(choice)

if __name__ == '__main__':
    test_card = Card()
    while (True):
        choice = menu()
        if (choice == 1):
            test_card.generate_card()
        elif (choice == 2):
            test_card.print_card()
        elif (choice == 3):
            sys.exit()
