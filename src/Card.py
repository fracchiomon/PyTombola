"""each Card contains 15 numbers (3 ROWS, 5 numbers per line)
the 5 numbers on each row must be in ascending order
a number cannot appear more than once per card
all numbers from 1 to 90 must be used with the same frequency
on the same line there cannot be two numbers of the same "ten".
  (by tens we mean: 1-10 ; 11-20 ; 21-30 ; ... ; 81-90)"""

import numpy as np
from Draws import Draws


class Card:
    ID_MAX_NUMBER = pow(2, 16)  # a little flex just because we can. But this should be the  Card number.
    ROWS = 3
    COLUMNS = 5
    SIZE = 15
    LOWER_BOUND = 1
    UPPER_BOUND = 91

    id = hex(0)
    card_numbers = None
    rng = None

    def __init__(self):
        # start random number generation
        self.rng = np.random.default_rng()
        numbers = self.rng.choice(
            range(self.LOWER_BOUND, self.UPPER_BOUND), self.SIZE, replace=False)
        self.id = hex(self.rng.integers(
            low=0, high=self.ID_MAX_NUMBER, dtype=int))
        self.card_numbers = np.array([[], []], dtype=int)

        # suddivido il vettore dei numeri casuali tra tre array che saranno le ROWS della Card
        # li ordino in ordine ascendente tramite funzione Sorted che di default opera in chiave ascendente
        # self.riga1 = (sorted(numbers[0:9]))   #anteporre np.array per renderlo array vero e proprio
        # self.riga2 = (sorted(numbers[9:18]))    #altrimenti le tre ROWS sono oggetti List
        # self.riga3 = (sorted(numbers[18:27]))
        # coso = '[]'

    def get_card_id(self):
        return self.id

    def get_ROWS(self):
        return self.ROWS

    def get_COLUMNS(self):
        return self.COLUMNS

    def get_card_numbers(self):
        return self.card_numbers

    def set_card_numbers(self, matrix):
        self.card_numbers = np.array(matrix, dtype=int)

    def print_card(self):
        matrix = self.get_card_numbers()

        print(self.get_card_id())
        print("\n\n")
        print(matrix)

    def generate_card(self):
        """creation of Card tuple"""
        """Thanks to GitHub user @francinicla for the original methods genera_Card and his nice attempt with Python Tombola-Bingo"""

        num = Draws()
        matrix = num.matrix(self.UPPER_BOUND - 1)
        card_tuple = [matrix]
        cmatrix = matrix

        for a in range(1, 4):
            row = np.array([], dtype=int)
            matrix_of_values = []
            matrix_of_values += cmatrix
            for b in range(1, 6):
                numbers_to_draw = []
                for h in range(0, 90):
                    if matrix_of_values[h] != ' ':
                        value = matrix_of_values[h]
                        numbers_to_draw += value,
                choice = self.rng.choice(numbers_to_draw, replace=False)

                # row += choice, #?????????????
                np.append(row, choice)

                if choice < 10:
                    for g in range(0, 9):
                        matrix_of_values[g] = ' '
                elif 10 <= choice < 20:
                    for g in range(9, 19):
                        matrix_of_values[g] = ' '
                elif 20 <= choice < 30:
                    for g in range(19, 29):
                        matrix_of_values[g] = ' '
                elif 30 <= choice < 40:
                    for g in range(29, 39):
                        matrix_of_values[g] = ' '
                elif 40 <= choice < 50:
                    for g in range(39, 49):
                        matrix_of_values[g] = ' '
                elif 50 <= choice < 60:
                    for g in range(49, 59):
                        matrix_of_values[g] = ' '
                elif 60 <= choice < 70:
                    for g in range(59, 69):
                        matrix_of_values[g] = ' '
                elif 70 <= choice < 80:
                    for g in range(69, 79):
                        matrix_of_values[g] = ' '
                elif 80 <= choice <= 90:
                    for g in range(79, 90):
                        matrix_of_values[g] = ' '
                decrease = choice - 1
                cmatrix[decrease] = ' '
                np.sort(row)

        """Generazione COLUMNS in ordine crescente"""

        for m in range(1,9):
            supp_list = []
            found = 0
            if m == 8:
                for y in range(self.ROWS):
                    for x in range(self.COLUMNS):
                        if card_tuple[y][x] >= 80 and card_tuple[y][x] <= 90:
                            found += 1
                            supp_list.extend([y, x])

            else:
                for y in range(self.ROWS):
                    for x in range(self.COLUMNS):
                        if card_tuple[y][x] >= (10 * m) and card_tuple[y][x] <= (9 + (10 * m)):
                            found += 1
                            supp_list.extend([y, x])

            if found > 1:
                if found == 2:
                    if card_tuple[supp_list[0][0]][supp_list[0][1]] > card_tuple[supp_list[1][0]][supp_list[1][1]]:
                        pos1 = card_tuple[supp_list[0][0]][supp_list[0][1]]

                        card_tuple[supp_list[0][0]][supp_list[0][1]
                                                    ] = card_tuple[supp_list[1][0]][supp_list[1][1]]

                        card_tuple[supp_list[1][0]][supp_list[1][1]] = pos1

                    found = 0
                    supp_list = []

                if found == 3:
                    if card_tuple[supp_list[0][0]][supp_list[0][1]] > card_tuple[supp_list[1][0]][supp_list[1][1]]:
                        pos1 = card_tuple[supp_list[0][0]][supp_list[0][1]]

                        card_tuple[supp_list[0][0]][supp_list[0][1]
                                                    ] = card_tuple[supp_list[1][0]][supp_list[1][1]]

                        card_tuple[supp_list[1][0]][supp_list[1][1]] = pos1

                    if card_tuple[supp_list[1][0]][supp_list[1][1]] > card_tuple[supp_list[2][0]][supp_list[2][1]]:
                        pos1 = card_tuple[supp_list[1][0]][supp_list[1][1]]

                        card_tuple[supp_list[1][0]][supp_list[1][1]
                                                    ] = card_tuple[supp_list[2][0]][supp_list[2][1]]
                        card_tuple[supp_list[2][0]][supp_list[2][1]] = pos1
                    if card_tuple[supp_list[0][0]][supp_list[0][1]] > card_tuple[supp_list[1][0]][supp_list[1][1]]:
                        pos1 = card_tuple[supp_list[0][0]][supp_list[0][1]]

                        card_tuple[supp_list[0][0]][supp_list[0][1]
                                                    ] = card_tuple[supp_list[1][0]][supp_list[1][1]]

                        card_tuple[supp_list[1][0]][supp_list[1][1]] = pos1

                    found = 0
                    supp_list = []

        # return card_tuple
        self.set_card_numbers(card_tuple)


