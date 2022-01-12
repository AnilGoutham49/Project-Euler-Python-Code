import csv

file = open('thirteen.csv', 'r')
csv_reader = csv.reader(file)
list = []

for row in csv_reader:
    list.append(row[0])

for ind, ele in enumerate(list):
    list[ind] = int(ele)

total = sum(list)
print(total)
