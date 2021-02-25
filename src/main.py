import numpy as np
import sys
from Cartella import *
from Estrazioni import *

def menu():
    print("Cosa fare?\n")
    print("1: Genera Cartella\n2: Stampa Cartella\n3: Esci\n\n")
    choice = input()
    return int(choice)

if __name__ == '__main__':
    cartella_prova = Cartella()
    while (True):
        choice = menu()
        if (choice == 1):
            cartella_prova.genera_cartella()
        elif (choice == 2):
            cartella_prova.stampa()
        elif (choice == 3):
            sys.exit()
