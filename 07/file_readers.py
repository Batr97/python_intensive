import json
import csv


class BaseReader:
    def read(self, ):
        raise NotImplementedError


class BaseWriter:
    def dump(self,):
        raise NotImplementedError


class TxtReader(BaseReader):
    def read(self, fileobj):
        with open(fileobj, 'r') as f:
            data = f.readlines()
        return data


class TxtWriter(BaseWriter):
    def dump(self, fileobj, data):
        with open(fileobj, 'w') as f:
            f.write(data)


class JSNReader(BaseReader):
    def read(self, fileobj):
        with open(fileobj) as f:
            data = json.load(f)
            return data


class JSNWriter(BaseWriter):
    def dump(self, fileobj, data):
        with open(fileobj, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


class CSVReader(BaseReader):
    def read(self, fileobj):
        with open(fileobj) as f:
            reader = csv.reader(f, delimiter=",", quotechar='"')
            # next(reader, None)  # skip the headers
            data = [row for row in reader]
        return data


class CSVWriter(BaseWriter):
    def dump(self, fileobj, data):
        with open(fileobj, "wt") as f:
            writer = csv.writer(f, delimiter=",")
            # writer.writerow(["your", "header", "foo"])  # write header
            writer.writerows(data)


# использование
def read_data(fileobj, reader: BaseReader):
    # возвращает распаршенные данные
    if isinstance(reader, TxtReader):
        data = reader.read(fileobj)
    elif isinstance(reader, JSNReader):
        data = reader.read(fileobj)
    elif isinstance(reader, CSVReader):
        data = reader.read(fileobj)
    return data


def dump_data(data, fileobj, writer: BaseWriter):
    if isinstance(writer, TxtWriter):
        writer.dump(fileobj, data)
    if isinstance(writer, JSNWriter):
        writer.dump(fileobj, data)
    if isinstance(writer, CSVWriter):
        writer.dump(fileobj, data)
