import csv
import os


#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Election_Analysis", "Resources", "election_results.csv")


#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Election_Analysis", "analysis", "election_analysis.txt")

#  Initialize a total vote counter.
total_votes = 0

#Declare a new list, candidate_options = [] by adding it here.
candidate_options = []
#Declare an empty dictionary to count votes per candidate
candidate_votes = {}

#Open the election results and read the file.
with open(file_to_load) as election_data:
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read and print the header row.
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        
        #  Add to the total cote count.
        total_votes += 1  # This statement is the same as total_votes = total_votes + 1
        
        #Get the candidate's name from the row within the for loop
        candidate_name = row[2]


        #Check for candidate in candidate_options list
        if candidate_name not in candidate_options:
        
            #Add the candidate name to the candidate_options list using the append() method.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] += 1



#Print the candidate vote dictionary.
print(candidate_votes)

#Get % per candidate
# 1. Iterate through list
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the % of votes
    vote_percentage = (float(votes) / float(total_votes)) * 100
    # 4. Print the candidate name and percentage vote
    print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")
