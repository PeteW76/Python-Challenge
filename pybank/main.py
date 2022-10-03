#Imports for working with CSV Files
import os
import csv

#Path to CSV
bank_report_csv = os.path.join("Resources", "budget_data.csv")

# Global Variables
#Count of Months row [0]
individual_months = 0

#Sum of total profits row[1]
net_total_profits = 0

#Variable that will be placed at the end of the loop that will hold the profit/loss value from the previous
#month and allow us to calucate change. (Initial value is set to zero)
math_month = 0

#Change in profits between months. (Initial value is set to zero)
PL_Change = 0

#Sum of profits/losses between months. (Initial value is set to zero)
PL_Track = 0

#Avg of PL_Track. (Initial value is set to zero)
PL_Avg_Change = 0

#The greatest value for PL_Change. (Initial value is set to zero)
PL_Positive = 0

#The month were the greatest Value for PL_Change took place
PL_Positive_Month = ""

#The lowest value for PL_Change. (Initial value is set to zero)
PL_Negative = 0

#The month were the greatest Value for PL_Change took place
PL_Negative_Month = ""

#Open the CSV file
with open(bank_report_csv) as bank_csv:
    bankcsvreader = csv.reader(bank_csv, delimiter=",")
    #Skip the column headers
    bankcsvheader = next(bankcsvreader)
    
    for row in bankcsvreader:
        #This will set our first math_month as the first value in row[1]
        if bankcsvreader.line_num == 2:
            math_month = int(row[1])
        #This will give us a count of all the months in the CSV file. This works because each
        #month has its own row and no months repeat. If we had repeating months we would need
        #a different solution. This returns a defacto row count
        individual_months = int(individual_months) +1
        #Sum of Profits and Losses row[1]
        net_total_profits = net_total_profits + int(row[1])
        #Change of profits between months
        PL_Change =  int(row[1]) - int(math_month)
        #Sum of PL_Changes between months
        PL_Track = PL_Track + PL_Change
        #The if statement returns the LARGEST value in PL_Change
        #and the corresponding month
        if PL_Positive < PL_Change:
            PL_Positive = PL_Change
            PL_Positive_Month = row[0]
        #The if statement returns the SMALLEST value in PL_Change
        #and the corresponding month
        if PL_Negative > PL_Change:
            PL_Negative = PL_Change
            PL_Negative_Month = row[0]

        #Sets math_month to row[1] of the current iteration of the loop. This causes this value to be
        #subtracted from subsequent iterations of row[1] and those subsequent values to be defined in
        #math_month. This allows us to calculate values for all the variables that start with "PL"
        math_month = int(row[1])
        
#Formatted Average for Profit/Loss changes. Of note is the use of individual_months as a divisor. Because,
# in this CSV, each month is unique and occurs only once, this variable also equals a row count. If this 
# was not the case, the wrong value would be returned. Also, the there is no actual calculation for the first
#month, math_month will subtract from itself and equal 0. In order for the average to be correct 1 must 
#be subtracted from individual_month. 86 rows but 85 calculations.
PL_Avg_Change = round(PL_Track / (individual_months -1),2)

# Print statments    
print(f"Total Months: {individual_months}")
print(f"Total {net_total_profits}")
print(f"Average Change: {PL_Avg_Change}")
print(f"Greatest Increase in Profits: {PL_Positive_Month} {PL_Positive}")
print(f"Greatest Decrease in Profits: {PL_Negative_Month} {PL_Negative}")

#Export to a text file
with open('Analysis/pybank.txt', 'w') as f:
    f.write(f"Total Months: {individual_months}")
    f.write("\n")
    f.write(f"Total {net_total_profits}")
    f.write("\n")
    f.write(f"Average Change: {PL_Avg_Change}")
    f.write("\n")
    f.write(f"Greatest Increase in Profits: {PL_Positive_Month} {PL_Positive}")
    f.write("\n")
    f.write(f"Greatest Decrease in Profits: {PL_Negative_Month} {PL_Negative}")
  