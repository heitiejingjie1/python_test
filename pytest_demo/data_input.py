import csv


def data_f(path):
    csv_data = open(path)

    data = csv.reader(csv_data)

    return list(data)[1:]
