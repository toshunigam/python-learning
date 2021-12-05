# Python program to demonstrate
# writing to CSV

import csv

header = ["Name","Email","Age"]
Values = [
    "Toshu",
    "ToshuNigam@ymail.com",
    34
]
filename = 'mycsvfile.csv'

with open(filename,"w") as csvfile:
    csvObj = csv.writer(csvfile)
    csvObj.writerow(header)
    csvObj.writerow(Values)

file = open(filename,"r")

for row in file:
    print(row)
