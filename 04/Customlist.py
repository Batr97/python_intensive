class Customlist(list):
    def __str__(self):
        lst = self.copy()
        return f'{lst} has the sum {sum(lst)}'

    def compare(self):
        return sum(self)

    def extension(self, n):
        lst = self.copy()
        lst.extend([0]*n)
        return lst

    def __add__(self, other):
        if not isinstance(other, Customlist):
            other = Customlist(other)
        lst = self.copy()
        lst2 = other.copy()
        if len(other) < len(self):
            n = len(self) - len(other)
            lst2 = other.extension(n)
        elif len(other) > len(self):
            n = len(other) - len(self)
            lst = self.extension(n)
        return Customlist([a_i + b_i for a_i, b_i in zip(lst, lst2)])

    def __radd__(self, other):
        if not isinstance(other, Customlist):
            other = Customlist(other)
        lst = self.copy()
        lst2 = other.copy()
        if len(other) < len(self):
            N = len(self) - len(other)
            lst2 = other.extension(N)
        elif len(other) > len(self):
            N = len(other) - len(self)
            lst = self.extension(N)
        return Customlist([a_i + b_i for a_i, b_i in zip(lst, lst2)])

    def __sub__(self, other):
        if not isinstance(other, Customlist):
            other = Customlist(other)
        lst = self.copy()
        lst2 = other.copy()
        if len(other) < len(self):
            N = len(self) - len(other)
            lst2 = other.extension(N)
        elif len(other) > len(self):
            N = len(other) - len(self)
            lst = self.extension(N)
        return Customlist([a_i - b_i for a_i, b_i in zip(lst, lst2)])

    def __rsub__(self, other):
        if not isinstance(other, Customlist):
            other = Customlist(other)
        lst = self.copy()
        lst2 = other.copy()
        if len(other) < len(self):
            N = len(self) - len(other)
            lst2 = other.extension(N)
        elif len(other) > len(self):
            N = len(other) - len(self)
            lst = self.extension(N)
        return Customlist([a_i - b_i for a_i, b_i in zip(lst2, lst)])

    def __eq__(self, other):
        return self.compare() == other.compare()

    def __ne__(self, other):
        return self.compare() != other.compare()

    def __lt__(self, other):
        return self.compare() < other.compare()

    def __le__(self, other):
        return self.compare() <= other.compare()

    def __gt__(self, other):
        return self.compare() > other.compare()

    def __ge__(self, other):
        return self.compare() >= other.compare()