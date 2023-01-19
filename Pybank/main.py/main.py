##Python Challenge 

#impot os and csv
import os
import csv

#Set the path for the csv file 
cvsfile = os.path.join('..', 'Resources', 'budget_data.csv')
with open('budget_data.csv','newfile') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    
    #create empty lists to add the csv values to 
    month_count = []
    profit = []
    change_inprofit = []
    
                      
    #iterate through the values and add them to the empty list 
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit) -1):
        change_inprofit.append(profit[i+1]-profit[i])
                      
#Evaluate the max and min from the list made
increase = max(change_inprofit)
decrease = min(change_inprofit)

#Using the index, 
month_increase = change_inprofit.index(max(change_inprofit))+1
month_decrease = change_inprofit.index(min(change_inprofit))+1


print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_inprofit)/len(change_inprofit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")      

output = os.path.join(".", 'output.txt')
with open(output,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("------------------------")
    file.write("\n")
    file.write(f"Total Months:{len(month_count)}")
    file.write("\n")
    file.write(f"Total: ${sum(profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(change_inprofit)/len(change_inprofit),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")