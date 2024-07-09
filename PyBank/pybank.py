#!/usr/bin/env python
# coding: utf-8

# In[55]:


# Importing Dependencies
import csv
import os

# Output to take the format below
#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)

# File load path and output file

file_load = os.path.join(".","Resources","budget_data.csv")
file_output = os.path.join(".","budget_analysis.txt")

# Define variables to count total Months, net profit and loss, 
total_months = 1
net = 0
net_change = 0
previous_net = 0
net_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",9999999999]

# reads budget_data.csv and converts it into a list
with open(file_load) as dates_profits_losses_raw:
    reader = csv.reader(dates_profits_losses_raw)
  

    #read the header row
    header = next(reader)
    #Read Fist Row of Price Data   
    first_row = next(reader)
    net += int(first_row[1])
    previous_net = int(first_row[1])
    
    
    #Now to loop through the data
    
    for row in reader:
        #each row of the data is a month, this adds 1 month to the total months per row
        total_months += 1
        
        #Net will like wise be added up using the data in coulumn 1
        net += int(row[1])
        
        #Track the profit and loss change in a list, to be used for biggest increase and decresase
        net_change = int(row[1])-previous_net
        previous_net = int(row[1])
        net_change_list.append(net_change)

        #Find month and Value of greatst increase in profits
        if(net_change > greatest_increase[1]):
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change


        #Find month and Value of greatst decrease in profits
        if(net_change < greatest_decrease[1]):
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

#print(greatest_increase)
#print(greatest_decrease)

average_change = sum(net_change_list)/len(net_change_list)
output = (
    f"Financial Analysis\n"
    f"------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)

with open(file_output, "w") as txt_file:
    txt_file.write(output)


# In[ ]:




