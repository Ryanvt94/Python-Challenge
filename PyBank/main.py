#PyBank
import csv
import os

bank_path = os.path.join('..', r'PyBank\Resources', 'pybank_budget_data.csv')

greatest_increase = {"Month": "", "Value": 0}
greatest_decrease = {"Month": "", "Value": 0}

# total number of months
def count(bank_data):
    with open(bank_data, 'r') as bankfile:

        bankreader = csv.reader(bankfile)
        header = next(bankreader)
        return sum([1 for row in bankreader])
        
total_months = count(bank_path)

# net total amount for profit/losses
def total(bank_data):
    with open(bank_data, 'r') as bankfile:

        bankreader = csv.reader(bankfile)
        header = next(bankreader)
        return sum([int(row[1]) for row in bankreader])
    
total_profit = total(bank_path)

# changes in profit/losses
def change(bank_data):
    with open(bank_data, 'r') as bankfile:
            
        bankreader = csv.reader(bankfile)
        header = next(bankreader)

        previous_value = int(next(bankreader)[1])
        diff_count = 0

        for row in bankreader:
            current_value = int(row[1])
            diff_count += 1
    
    return (current_value - previous_value) / diff_count

average_change = change(bank_path)

# greatest increase and decrease
with open(bank_path, 'r') as bankfile:

    bankreader = csv.reader(bankfile)
    header = next(bankreader)
    for row in bankreader:
        if greatest_increase["Value"] < int(row[1]):
            greatest_increase["Month"] = row[0]
            greatest_increase["Value"] = int(row[1])
        if greatest_decrease["Value"] > int(row[1]):
            greatest_decrease["Month"] = row[0]
            greatest_decrease["Value"] = int(row[1])

#summary table
output = (
    f'Financial Analysis\n'
    f'----------------------------\n'
    f'Total Months: {total_months}\n' 
    f'Total: ${total_profit}\n'
    f'Average Change: {average_change:2,.0f}\n' 
    f'Greastest Increase in Profits: {greatest_increase["Month"]}  (${greatest_increase["Value"]})\n' 
    f'Greastest Decrease in Profits: {greatest_decrease["Month"]}  (${greatest_decrease["Value"]})\n'  
)
print(output)

# export file
output_file = os.path.join('..', 'PyBank', 'Analysis/budget_analysis.txt')

with open(output_file, "w") as datafile:
    datafile.write(output)

