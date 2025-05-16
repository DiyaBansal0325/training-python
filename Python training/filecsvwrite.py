import csv
f = open("color.csv","w")
writer = csv.writer(f)
writer.writerow(["red","green","blue"])
writer.writerow(["yellow","orange","white"])

#using a python program read the table present in mysql database and save the content into the file on desktop