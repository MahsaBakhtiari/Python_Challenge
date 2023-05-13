import os
import csv
import statistics


def read_file(file_address):
    """Loads the file and returns a header and file content."""
    file_list = []
    file_header = []
    with open(address, encoding="UTF-8") as file:
        reader = csv.reader(file, delimiter=",")
        # Read the first row and keep it as file header.
        file_header = next(reader, None)
        for row in reader:
            # Append a tuple (month, profit/loss).
            file_list.append((row[0], float(row[1])))
    return (file_header, file_list)

address = os.path.join(".", "Resources", "budget_data.csv")
result = read_file(address)

# Introduce pre_value as the last month's profit/loss. 
pre_value = result[1][0][1]
monthly_changes = []                            

# Start from the second month and compute the monthly changes.
for value in result[1][1:]:
    monthly_changes.append((value[0],(value[1] - pre_value)))
    pre_value = value[1]
                                
month_count = len(result[1])
total = sum([pair[1] for pair in result[1]])
monthly_changes_value = [pair[1] for pair in monthly_changes]
average_change = statistics.mean(monthly_changes_value)

# Finding the maximum ans minimum changes starting 
# from really big positive and negative numbers.
greatest_increase = ("a", -1e9)
greatest_decrease = ("b", 1e9)                            
for change in monthly_changes:
    if change[1] > greatest_increase[1]:
        greatest_increase = change
    if change[1] < greatest_increase[1]:
        greatest_decrease = change

print(f"Financial Analysis \n---------------------------------------------------")
print(f"Total Months: {month_count} \nTotal: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]}")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} ${greatest_decrease[1]}")

with open("PyBank.txt", "a") as f:
    f.write("Financial Analysis \n")
    f.write("--------------------------------------------------- \n")
    f.write(f"Total Months: {month_count} \n")
    f.write(f"Total: ${total} \n")
    f.write(f"Average Change: ${average_change} \n")
    f.write(f"Greatest Increase in Profits: {greatest_increase[0]} ${greatest_increase[1]} \n")
    f.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} ${greatest_decrease[1]} \n")
    
    
