#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initiazlize total vote counter
total_votes = 0

#Declare a new list
candidate_options = []
#Declare and empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = "" #This variable holds an empty string.
winning_count = 0
winning_percentage = 0


#Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read the file object with the read function.
    file_reader = csv.reader(election_data)

    #Read header row only
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader: #(indent after for!!!)
        #Add to the total vote count.
        total_votes += 1

        #Print candidate name from each row
        candidate_name = row[2]

        # If the candidate does not mach any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)

            #Begin tracking that candidates vote count
            candidate_votes[candidate_name] =0

            #Add a vote to that candidates count
        candidate_votes[candidate_name] += 1



#Determine the percent of votes for ea. candidate by looping thru the counts.
#1. Iterate thru the candidate list.
for candidate_name in candidate_votes:
    #2. Retreive vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    #4. Print the candidate name and percentage of votes.
    #print(f"{candidate_name}: received {vote_percentage}% of the vote.")

    # Print each candidates name, vote counte and % of votes.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #Determine winning vote count and candidate.
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #2. if true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidates name.
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"________________________\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"________________________\n")
print(winning_candidate_summary)

#Print the candidate list (candidate_names), votes (candidate_votes).
#print(candidate_votes)
