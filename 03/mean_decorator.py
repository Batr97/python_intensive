import time


class DecoratorArgs:
    def __init__(self, k):
        self.time_saver = []
        self.k = k

    def __call__(self, func):
        def wrapper(n):
            start = time.perf_counter()
            func(n)
            end = time.perf_counter()
            self.time_saver.append(end-start)
        return wrapper



