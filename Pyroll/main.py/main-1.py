#PyPoll Challenge

#Import os and csv
import os
import csv

#Set the path for the csv file 
csvfile = os.path.join('election_data.csv')

#Make directory for candidate's name/vote count for, set total votes to zero for count
poll = {}
total_votes = 0

#Retrieve data file, and open
with open (csvfile, newline=",") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    #create list for candidates/votes
    total_votes = 0 
    candidate_name = []
    candidate_list = []
    candidate_vote = []
    vote_counts = []
    vote_percent = []
    winner_votes = []


#Winning candidate/Winning Count
winning_candidate = ""
winning_count = 0

#For all row individually 
for row in csvreader:
    print(". ", end="")
    total_votes = total_votes + 1
    candidate_list= row["Candidate"]

    #If candidate does not match exisiting candidate, add it to the list of candidates:
    if candidate_list in candidate_name:
        vote_counts[candidate_name] = vote_counts[candidate_name] + 1

    else:
        candidate_list.append(candidate_name)
        vote_counts(candidate_name)  

    #Loop thorough each candidate to get percentage of vote
    for key, value in vote_counts.items():
        vote_counts.append(value)
        vote_counts = candidate_vote[candidate_name]
        vote_percent = round((int(value)/total_votes * 100),2)
        vote_percent.append(vote_percent) 

    #Identify the winner
    if (value > winner_votes):
        winner_votes = value
        winner = key

#Combination of lists to 1 print
Output = zip(candidate_list, vote_percent, vote_counts)
Output = list(Output)

print("Poll Results")
print("----------------")
print(f'Total Votes: {total_votes}')
print("----------------")
for item in Output:
    print(f'{item[0]} : {item[1]}0% ({item [2]})')
print('----------------')
print(f'Winner : {winner}')
print('----------------')

#Create an output.file and export the result as csv file
output_file = os.path.join("pyroll_results.csv")
with open(output_file,"w",newline='') as datafile:
    writer = csv.writer('datafile')

output_file = os.path.join("pyroll_results.csv")
with open(output_file,"w",newline="") as datafile:
    csvwriter = csv.writer(datafile)

csvwriter.writerow(["Election Results"])
csvwriter.writerow(['------------------'])
csvwriter([f'Total votes : {total_votes}'])
csvwriter.writerow('[------------------]')
for item in Output:
    csvwriter.writerow([f'{item[0]} : {item[1]}00% ({item[2]})'])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f'Winner : {winner}'])
    csvwriter.writerow(["-------------------------"])
    
    















