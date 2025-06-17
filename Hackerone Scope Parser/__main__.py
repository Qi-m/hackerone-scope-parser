import csv
import re

file_name = input("File Name: ")
finalList = []

with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for l in csv_reader:
        if l[1] in ('WILDCARD', 'URL'):
            finalList.append(l[0])

if finalList:
    finalList.pop(0)

output_file_name = input("Output File Name: ")

wildcard_question = input("Wildcard only file?(y/N): ").lower()
if wildcard_question == "y":
    wildcard_file_name = input("Wildcard Only File Name: ")
    with open(wildcard_file_name, 'w') as wildcards:
        for i in finalList:
            match = re.search(r'^\*\.(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$', i)
            if match:
                wildcards.write(i + '\n')

else:
    print("No Wildcard Only File created!")

with open(output_file_name, 'w') as output:
    for i in finalList:
        output.write(i + '\n')   
