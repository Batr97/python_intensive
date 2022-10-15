class Customlist(list):
    def __init__(self, lst):
        super().__init__()
        self.lst = lst

    def __str__(self):
        return f'list is following {self.lst} and the sum {self.compare(self.lst)}'

    def compare(self, lst):
        return sum(lst)

    def extension(self, lst, n):
        return lst + [0,] * n

    def __add__(self, other):
        if not isinstance(other, Customlist):
            other = Customlist(other)
        if len(other.lst) < len(self.lst):
            n = len(self.lst) - len(other.lst)
            other.lst = self.extension(other.lst, n)
        elif len(other.lst) > len(self.lst):
            n = len(other.lst) - len(self.lst)
            self.lst = self.extension(self.lst, n)
        return Customlist([a_i + b_i for a_i, b_i in zip(self.lst, other.lst)])
    
    def __radd__(self, other):
        if not isinstance(other, Customlist):
            other = Customlist(other)
        if len(other.lst) < len(self.lst):
            n = len(self.lst) - len(other.lst)
            other.lst = self.extension(other.lst, n)
        elif len(other.lst) > len(self.lst):
            n = len(other.lst) - len(self.lst)
            self.lst = self.extension(self.lst, n)
        return Customlist([a_i + b_i for a_i, b_i in zip(self.lst, other.lst)])        
        
    def __sub__(self, other):
        if not isinstance(other, Customlist):
            other = Customlist(other)
        if len(other.lst) < len(self.lst):
            n = len(self.lst) - len(other.lst)
            other.lst = self.extension(other.lst, n)
        elif len(other.lst) > len(self.lst):
            n = len(other.lst) - len(self.lst)
            self.lst = self.extension(self.lst, n)
        return Customlist([a_i - b_i for a_i, b_i in zip(self.lst, other.lst)])

    def __rsub__(self, other):
        if not isinstance(other, Customlist):
            other = Customlist(other)
        if len(other.lst) < len(self.lst):
            n = len(self.lst) - len(other.lst)
            other.lst = self.extension(other.lst, n)
        elif len(other.lst) > len(self.lst):
            n = len(other.lst) - len(self.lst)
            self.lst = self.extension(self.lst, n)
        return Customlist([a_i - b_i for a_i, b_i in zip(other.lst, self.lst)])

    def __eq__(self, other):
        return self.compare(self.lst) == self.compare(other.lst)

    def __ne__(self, other):
        return self.compare(self.lst) != self.compare(other.lst)   

    def __lt__(self, other):
        return self.compare(self.lst) < self.compare(other.lst)        
    
    def __le__(self, other):
        return self.compare(self.lst) <= self.compare(other.lst)

    def __gt__(self, other):
        return self.compare(self.lst) > self.compare(other.lst)

    def __ge__(self, other):
        return self.compare(self.lst) >= self.compare(other.lst)
                             

    

