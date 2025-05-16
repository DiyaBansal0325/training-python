import csv
file = open("color.csv","r")
r = csv.reader(file)
for row in r:
    print(row)
    for i in row:
        print(i)
