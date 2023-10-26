def read_csv_file(filename):
    from csv import DictReader
    csv_file = open(filename, "r")
    file_reader = DictReader(csv_file)
    return list(file_reader)


print(read_csv_file("people.csv"))
