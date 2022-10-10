import functools
import time

def my_decorator(arg):
    def inner_decorator(f):
        @functools.wraps(f)
        def wrapped(*args, **kwargs):
            lst = []
            for i in range(100):
                if i >= (100-arg):
                    start = time.perf_counter()
                    response = f(*args, **kwargs)
                    end = time.perf_counter()
                    lst.append(end-start)
            return f'среднее время выполнения {arg} запросов для {f.__name__!r}: {sum(lst)/len(lst)} сек'
        return wrapped
    return inner_decorator

@my_decorator(500)
def foo(n):
    return 2 ** n

@my_decorator(2)
def boo(n):
    return [0] * n

print(foo(500))
print(boo(2))
