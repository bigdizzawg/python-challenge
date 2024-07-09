#!/usr/bin/env python
# coding: utf-8

# In[43]:


import csv
import os

#setting import and output file paths
import_file = os.path.join(".", "Resources", 'election_data.csv')

output_file = os.path.join(".","election_analysis.txt")

# creating total votes Counter
total_votes = 0

# creating dictionary for candidate votes
candidate_votes = {}
# Creating counters for candidate names, winning count, and winning candidate
candidate_names = []
winning_count = 0
winning_candidate = ""

with open(import_file) as election_data:
    #reads the data   
    reader = csv.reader(election_data)
    #reads the header
    header = next(reader)
    

#looping through the data    
    for row in reader:
        #counts all the votes
        total_votes = total_votes+1

        #pulls the candidate name from each row
        candidate_name = row[2]

        #if candidate does not match any existing candidate, discovers candidate name
        if candidate_name not in candidate_names:
            #adds it to the list of candidates 
            candidate_names.append(candidate_name)
            
            #initializing the dictionary to candidate names with 
            candidate_votes[candidate_name] = 0
            
            #counts each candidates' votes
        candidate_votes[candidate_name] += 1
    
   

# defining output, writing to file and printing it
with open(output_file,"w") as txt_file:
    output = (
        f"Election Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"------------------------\n"
            )
    print(output, end="")
    txt_file.write(output)

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        if(votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        txt_file.write(voter_output)
        print(voter_output)

winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"------------------------\n"
    )   
print(winning_candidate_summary)

txt_file.write(winning_candidate_summary)
#Election Results
#-------------------------
#Total Votes: 369711
#-------------------------
#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)
#-------------------------
#Winner: Diana DeGette
#-------------------------


# In[ ]:




