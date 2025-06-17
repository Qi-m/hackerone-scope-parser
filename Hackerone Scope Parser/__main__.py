import csv

file_name = input("File Name: ")
finalList = []

with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for l in csv_reader:
        if l[1] in ('WILDCARD', 'URL'):
            finalList.append(l[0])
finalList.pop(0)

output_file_name = input("Output File Name: ")

with open(output_file_name, 'w') as output:
    for i in finalList:
        output.write(i + '\n')   
