"""ogni cartella contiene 15 numeri (3 ROWS, 5 numeri per riga)
i 5 numeri su ogni riga devono essere in ordine crescente
un numero non puo' comparire piu' di una volta per cartella
devono essere usati tutti i numeri da 1 a 90 con la stessa frequenza
sulla stessa riga non ci possono essere due numeri della stessa "decina"
  (per decina si intende: 1-10 ; 11-20 ; 21-30 ; ... ; 81-90)"""

import numpy as np
from Estrazioni import Estrazioni


class Cartella:
    ID_MAX_NUMBER = pow(2, 16)
    ROWS = 3
    COLUMNS = 5
    SIZE = 15
    LOWER_BOUND = 1
    UPPER_BOUND = 91

    id = hex(0)
    numeri_cartella = None
    rng = None

    def get_cartella_number(self):
        return self.id

    def get_ROWS(self):
        return self.ROWS

    def get_COLUMNS(self):
        return self.COLUMNS

    def get_numeri_cartella(self):
        return self.numeri_cartella

    def set_numeri_cartella(self, matrice):
        self.numeri_cartella = np.array(matrice, dtype=int)

    def __init__(self):
        # start random number generation
        self.rng = np.random.default_rng()
        numbers = self.rng.choice(
            range(self.LOWER_BOUND, self.UPPER_BOUND), self.SIZE, replace=False)
        self.id = hex(self.rng.integers(
            low=0, high=self.ID_MAX_NUMBER, dtype=int))
        self.numeri_cartella = np.array([[], []], dtype=int)

        # suddivido il vettore dei numeri casuali tra tre array che saranno le ROWS della cartella
        # li ordino in ordine ascendente tramite funzione Sorted che di default opera in chiave ascendente
        # self.riga1 = (sorted(numbers[0:9]))   #anteporre np.array per renderlo array vero e proprio
        # self.riga2 = (sorted(numbers[9:18]))    #altrimenti le tre ROWS sono oggetti List
        # self.riga3 = (sorted(numbers[18:27]))
        # coso = '[]'

    def genera_cartella(self):
        """ creazione della tupla della cartella elemento output = tupla cartella generata"""
        """Thanks to GitHub user @francinicla for the original methods genera_cartella and his nice attempt with Python Tombola-Bingo"""

        num = Estrazioni()
        matrix = num.matrix(self.UPPER_BOUND - 1)
        tupla_cartella = np.array([], dtype=int)
        cmatrice = matrix

        for a in range(1, 4):
            row = np.array([], dtype=int)
            matrix_of_values = []
            matrix_of_values += cmatrice
            for b in range(1, 6):
                numbers_to_draw = []
                for h in range(0, 90):
                    if matrix_of_values[h] != ' ':
                        value = matrix_of_values[h]
                        numbers_to_draw += value,
                scelto = self.rng.choice(numbers_to_draw, replace=False)

                #row += scelto, #?????????????
                np.append(row,scelto)

                if scelto < 10:
                    for g in range(0, 9):
                        matrix_of_values[g] = ' '
                elif 10 <= scelto < 20:
                    for g in range(9, 19):
                        matrix_of_values[g] = ' '
                elif 20 <= scelto < 30:
                    for g in range(19, 29):
                        matrix_of_values[g] = ' '
                elif 30 <= scelto < 40:
                    for g in range(29, 39):
                        matrix_of_values[g] = ' '
                elif 40 <= scelto < 50:
                    for g in range(39, 49):
                        matrix_of_values[g] = ' '
                elif 50 <= scelto < 60:
                    for g in range(49, 59):
                        matrix_of_values[g] = ' '
                elif 60 <= scelto < 70:
                    for g in range(59, 69):
                        matrix_of_values[g] = ' '
                elif 70 <= scelto < 80:
                    for g in range(69, 79):
                        matrix_of_values[g] = ' '
                elif 80 <= scelto <= 90:
                    for g in range(79, 90):
                        matrix_of_values[g] = ' '
                decrease = scelto - 1
                cmatrice[decrease] = ' '
                np.sort(row)
            

        """Generazione COLUMNS in ordine crescente"""

        for m in range(9):
            primo = []
            trovati = 0
            if m == 8:
                for y in range(self.ROWS):
                    for x in range(self.COLUMNS):
                        if tupla_cartella[y][x] >= 80 and tupla_cartella[y][x] <= 90:
                            trovati += 1
                            primo.append([y, x])

            else:
                for y in range(1, self.ROWS+1):
                    for x in range(1, self.COLUMNS+1):
                        if tupla_cartella[y][x] >= (10 * m) and tupla_cartella[y][x] <= (9 + (10 * m)):
                            trovati += 1
                            primo.append([y, x])

            if trovati > 1:
                if trovati == 2:
                    if tupla_cartella[primo[0][0]][primo[0][1]] > tupla_cartella[primo[1][0]][primo[1][1]]:
                        pos1 = tupla_cartella[primo[0][0]][primo[0][1]]

                        tupla_cartella[primo[0][0]][primo[0][1]
                                                    ] = tupla_cartella[primo[1][0]][primo[1][1]]

                        tupla_cartella[primo[1][0]][primo[1][1]] = pos1

                    trovati = 0
                    primo = []

                if trovati == 3:
                    if tupla_cartella[primo[0][0]][primo[0][1]] > tupla_cartella[primo[1][0]][primo[1][1]]:
                        pos1 = tupla_cartella[primo[0][0]][primo[0][1]]

                        tupla_cartella[primo[0][0]][primo[0][1]
                                                    ] = tupla_cartella[primo[1][0]][primo[1][1]]

                        tupla_cartella[primo[1][0]][primo[1][1]] = pos1

                    if tupla_cartella[primo[1][0]][primo[1][1]] > tupla_cartella[primo[2][0]][primo[2][1]]:
                        pos1 = tupla_cartella[primo[1][0]][primo[1][1]]

                        tupla_cartella[primo[1][0]][primo[1][1]
                                                    ] = tupla_cartella[primo[2][0]][primo[2][1]]
                        tupla_cartella[primo[2][0]][primo[2][1]] = pos1
                    if tupla_cartella[primo[0][0]][primo[0][1]] > tupla_cartella[primo[1][0]][primo[1][1]]:
                        pos1 = tupla_cartella[primo[0][0]][primo[0][1]]

                        tupla_cartella[primo[0][0]][primo[0][1]
                                                    ] = tupla_cartella[primo[1][0]][primo[1][1]]

                        tupla_cartella[primo[1][0]][primo[1][1]] = pos1

                    trovati = 0
                    primo = []

        # return tupla_cartella
        self.set_numeri_cartella(tupla_cartella)

    def stampa(self):
        matrix = self.get_numeri_cartella()
        
        print(self.get_cartella_number())
        print("\n\n")
        print(matrix)

