from classes.Figura import Figura


class Triagle(Figura):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def count_p(self):
        perimetr = self.side1 + self.side2 + self.side3
        return perimetr
        # return self.side1 + self.side2 + self.side3



