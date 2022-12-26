import os
import csv

# Save the path for elections data csv file
budget = os.path.join('Resources','budget_data.csv')

# Read the path and the csv file
with open(budget) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Define the header in the csv file
    csv_header = next(csv_file)

    # Setup empty variables and lists
    change = 0
    date = []
    difference = []
    profit_loss = []

    # Iterate through each row and save the value of each row to empty lists
    for row in csv_reader:
        date.append(row[0])
        profit_loss.append(int(row[1]))

    # Save the total months and total profit/loss
    total_months = len(date)
    total_pl = sum(profit_loss)

    # Iterate through each element of the list and save the difference in a new list
    for i in range(len(profit_loss)):
        if i != 0:
            change = int(profit_loss[i]) - int(profit_loss[i-1])
            difference.append(change)

    # Calculate the average change
    avg_change = sum(difference)/len(difference)

    # Find the greatest increase and decrease value and month
    greatest_increase = max(difference)
    g_inc_index = difference.index(greatest_increase) + 1
    greatest_decrease = min(difference)
    g_dec_index = difference.index(greatest_decrease) + 1

    # Print the results
    print("Financial Analysis\n-------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_pl}")
    print("Average Change: $" + '%.2f' % avg_change)
    print(f"Greatest Increase in Profits: {date[g_inc_index]} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {date[g_dec_index]} (${greatest_decrease})")

# Create an output file and store the results there
with open("Analysis/budget_analysis.txt", "w") as f:
    print("Financial Analysis\n-------------------------", file = f)
    print(f"Total Months: {total_months}", file = f)
    print(f"Total: ${total_pl}", file = f)
    print("Average Change: $" + '%.2f' % avg_change, file = f)
    print(f"Greatest Increase in Profits: {date[g_inc_index]} (${greatest_increase})", file = f)
    print(f"Greatest Decrease in Profits: {date[g_dec_index]} (${greatest_decrease})", file = f)

    