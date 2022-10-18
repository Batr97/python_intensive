from file_readers import TxtReader, TxtWriter, JSNReader, JSNWriter, CSVReader, CSVWriter, read_data, dump_data
from generator import gen

dump_data({"x": "1"}, 'data1.json', writer=JSNWriter())
assert read_data('data1.json', reader=JSNReader()) == {"x": "1"}

dump_data('Hello world', 'data1.txt', writer=TxtWriter())
assert read_data('data1.txt', reader=TxtReader()) == ['Hello world']

dump_data(['hey', 'hi'], 'data1.csv', writer=CSVWriter())
assert read_data('data1.csv', reader=CSVReader()) == [['h', 'e', 'y'], ['h', 'i']]

FILENAME = 'data1_for_generator.txt'
lines = []
for line in gen(['Hello', 'bye'], FILENAME):
    lines.append(line.strip())
assert lines == ['Hello world', 'bye']
