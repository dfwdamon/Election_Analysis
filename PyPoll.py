#Add our dependencies
import csv
import os
#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initiazlize total vote counter
total_votes = 0

#Candidate options and candidate votes (Declare a new list)
candidate_options = []
#Declare and empty dictionary
candidate_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = "" #This variable holds an empty string.
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the read function.
    file_reader = csv.reader(election_data)

    # Read header row only
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader: #(indent after for!!!)
        #Add to the total vote count.
        total_votes += 1

        #Get the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not mach any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #Begin tracking that candidates vote count
            candidate_votes[candidate_name] =0

        #Add a vote to that candidates count
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # After opening the file print the final vote count to the terminal.
    election_results = (
            f"\nElection Results\n"
            f"__________________________\n"
            f"Total Votes. {total_votes:,}\n"
            f"__________________________\n")
    print(election_results, end ="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    #Determine the percent of votes for ea. candidate by looping thru the counts.
    #1. Iterate thru the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        #Determine winning vote count and candidate.
        # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #2. if true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    #print(f"{candidate_name}: received {vote_percentage}% of the vote.")
    winning_candidate_summary = (
        f"________________________\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"________________________\n")
    print(winning_candidate_summary)
    # Save the winning candidates results to the text file.
    txt_file.write(winning_candidate_summary)
