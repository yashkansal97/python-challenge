import os
import csv

budget = os.path.join('Resources','budget_data.csv')

with open(budget) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    total = 0
    change = 0
    date = []
    difference = []
    profit_loss = []

    for row in csv_reader:
        total = total + int(row[1])
        date.append(row[0])
        profit_loss.append(row[1])

    for i in range(len(date)):
        if i != 0:
            change = int(profit_loss[i]) - int(profit_loss[i-1])
            difference.append(change)

    print(range(len(date)+1))
    print(difference[0])
    print(min(difference))
    #print(sum(difference))
    print(sum(difference)/len(difference))



    #date = []

    #for col in csv_reader:
    #    date.append(col[0])

    #print(type(csv_reader))

    