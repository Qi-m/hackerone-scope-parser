import csv

file_name = input("File Name: ")
finalList = []

with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for l in csv_reader:
        finalList.append(l[0])
finalList.pop(0)

with open('output.txt', 'w') as output:
    for i in finalList:
        output.write(i + '\n')
        