class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if self.is_exists(side_a, side_b, side_c):
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c

    def is_exists(self, side_a, side_b, side_c):
        if side_a + side_b < side_c or \
                side_a + side_c < side_b \
                or side_b + side_c < side_a:
            raise ValueError('no such triangle exists')
        else:
            return True

    def is_right_angled(self):
        return self.side_a ** 2 + self.side_b ** 2 == self.side_c ** 2

    def _perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def __eq__(self, other):
        return self._perimeter() == other._perimeter()


tr1 = Triangle(3, 4, 5)
print(tr1.is_right_angled())
tr2 = Triangle(3, 4, 6)
print(tr2.is_right_angled())
print(tr1.__eq__(tr2))
