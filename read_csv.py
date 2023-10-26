def read_csv_file(filename):
    file = open(filename, "r")
    columns = file.readline().split(', ')
    data = []
    for x in file:
        # ['Andrew', 'Sheffield', '37']
        values = x.split(",")
        obj = {}
        for index, y in enumerate(values):
            obj.update({columns[index].strip(): values[index].strip()})
        data.append(obj)
    return data


data = read_csv_file("people.csv")

for item in data:
    print(item['name'])