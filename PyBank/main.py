import os
import csv

budget_csv = os.path.join(".", "resources", "budget_data.csv")


Total_Months = 0
Net_Total =  0
Average_Change = 0
Greatest_Profit_Increase = 0
Greatest_Profit_Decrease = 0
# lists to store data
Months = []
Profit_losses = []

# opening file/looping through csv

with open(budget_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    next(csvreader)

    for row in csvreader:
        Months.append(row[0])
        Profit_losses.append(float(row[1]))




    # get the total duration of data
total_months = (len(Months))
print(total_months)

# calculating sum total of profit losses
net_total = sum(Profit_losses)
print(Profit_losses)

# calculate the average change
average_change = net_total / total_months
print(average_change)

# calculate the greatest increase in profit
greatest_profit_increase = max(Profit_losses)
print(greatest_profit_increase)

# calculate the greatest decrease in profit
greatest_profit_decrease = min(Profit_losses)
print(greatest_profit_decrease)

max_index = Profit_losses.index(greatest_profit_increase)
maximum_month = Months[max_index] 

minimum_index = Profit_losses.index(greatest_profit_decrease)
minimum_month = Months[minimum_index]

# set up financial analysis output
Financial_Analysis = (f''' Financial Analysis
    Total Months: {total_months}
    Net Total: ${net_total:.2f}
    Average Change: {average_change:.2f}
    Greatest Increase in Profits: {maximum_month} {greatest_profit_increase:.2f}
    Greatest Decrease in Profit: {minimum_month} {greatest_profit_decrease:.2f} ''')



analysis = open('financial_analysis.txt', 'w')

analysis.write(Financial_Analysis) 