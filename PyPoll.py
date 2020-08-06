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

#Winning candidate tracker
winning_candidate = " "
winning_count = 0
winning_percentage = 0

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

    #Save the results to txt file
    with open(file_to_save, "w") as txt_file:
        
        #Print the vote count to the terminal
        election_results = (
            f"\nElection Results\n"
            f"---------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"---------------------------\n")
        print(election_results, end="")
        #Save the final vote count to the text file.
        txt_file.write(election_results)

        #Get % per candidate
        # 1. Iterate through list
        for candidate_name in candidate_votes:
            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # 3. Calculate the % of votes
            vote_percentage = (float(votes) / float(total_votes)) * 100
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            
            #Print each candidate's voter count and percentage to the terminal.
            print(candidate_results)
            #Save the candidate results to the text file
            txt_file.write(candidate_results)

            #Determine winning candidates
            #Determine if the votes is greater than the winning count.
            if(votes > winning_count) and (vote_percentage > winning_percentage):
                #if true set winning_count to votes and winning percent to vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name
                    
        #Winning Summary        
        winning_candidate_summary = (
            f"--------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Vote Percentage: {winning_percentage:.1f}%\n"
            f"---------------------------\n")
        print(winning_candidate_summary)

         #Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)

