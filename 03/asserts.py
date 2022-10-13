import json
import time
from parse_json import keyword_callback, parse_json
from mean_decorator import DecoratorArgs

json_str = """{
    "name": "jane_doe joe_black",
    "salary": "9000 4000 1000",
    "skills": "Raspberry_pi  Machine_Learning Web_Development",
    "email": "JaneDoe@pynative.com apple@mail.com dog@yandex.ru",
    "projects": "Python_Data_Mining Python_Data_Science"
}
"""

line1 = ['MACHINE_LEARNING', 'no keyword "Machine_Learning" for field "email"']
assert parse_json(json_str, keyword_callback, ['skills', 'email'], ['Machine_Learning']) == line1
line2 = 'no keywords were provided'
assert parse_json(json_str, keyword_callback, ['skills', 'email'], []) == line2
line3 = 'no required fields were provided'
assert parse_json(json_str, keyword_callback, [], ['skills']) == line3
assert parse_json(json_str, keyword_callback, [], []) == line3
line4 = 'hey'
assert keyword_callback(line4) == 'HEY'
line5 = 'HEY'
assert keyword_callback(line5) == 'HEY'


func1 = DecoratorArgs(10)
@func1
def foo(n):
    return [0] * n

for _ in range(20):
    foo(6)
time_exec_k = sum(func1.time_saver[-1:func1.k-1:-1])
length = len(func1.time_saver[-1:func1.k-1:-1])
print(f'average time of k function calls for foo is: {time_exec_k / length} sec')

func2 = DecoratorArgs(10)
@func2
def boo(n):
    return 2 ** n

for _ in range(200):
    boo(5)
time_exec_k = sum(func2.time_saver[-1:func2.k-1:-1])
length = len(func2.time_saver[-1:func2.k-1:-1])
print(f'average time of k function calls for boo is: {time_exec_k / length} sec')