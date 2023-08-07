from classes.Figura import Figura


class Rectangle(Figura):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def count_p(self):
        return (2 * self.side1) + (2 * self.side2)

