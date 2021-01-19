import numpy as np


class Estrazioni(object):
    numbers_to_draw = None  # numeri da pescare successivamente
    numbers_drawed = None  # numeri già pescati
    value = 0

    def get_numbers_to_draw(self):
        """standard Get method -> returns a Numpy Array"""
        return self.numbers_to_draw

    def get_numbers_drawed(self):
        """standard Get method -> returns a Numpy Array"""
        return self.numbers_drawed

    def set_numbers_to_draw(self, nparraymod):
        """standard Set method -> modifies a Numpy Array"""
        self.numbers_to_draw = nparraymod

    def set_numbers_drawed(self, nparraymod):
        """standard Set method -> modifies a Numpy Array"""
        self.numbers_drawed = nparraymod

    def __init__(self):
        """Class construction, rng generation and set methods calls invocation"""
        # start random number generation
        rng = np.random.default_rng()
        self.set_numbers_to_draw(np.arange(1, 91))  # generazione lista numeri
        self.set_numbers_drawed(np.array([], dtype=int))

    def draw(self):
        """Gestione estrazioni"""
        to_draw = self.get_numbers_to_draw()
        drawed = self.get_numbers_drawed()

        draw = self.rng.choice(range(1, 91), replace=False)
        self.set_numbers_drawed(np.append(drawed, draw))

        self.set_numbers_to_draw(
            np.delete(to_draw, np.argwhere(to_draw == draw)))

    def matrix(self, value):
        """ Matrix generator.\n
        input value = matrix size\n
        output value = matrix sized <tuple>
        """

        self.value = value + 1
        matrix = []
        for i in range(1, self.value):
            matrix.append(i)
        return matrix
