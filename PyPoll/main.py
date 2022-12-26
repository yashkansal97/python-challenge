import os
import csv

# Save the path for elections data csv file
polls = os.path.join('Resources','election_data.csv')

# Read the path and the csv file
with open(polls) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Define the header in the csv file
    csv_header = next(csv_file)

    # Create an empty list which will be used to store each vote from the csv file
    votes = []

    # Iterate through each row and append the votes file
    for row in csv_reader:
        votes.append(row[2])
    
    # Save the total number of votes
    total = len(votes)

    # Find the unique candidates and store them in a list
    candidates = list(set(votes))

    # Create empty lists to eventually store the votes for each candidate
    vote_count = []
    percentage_count = []

    # Create double for loops to iterate through each candidate and vote and count the votes for each candidate
    for i in range(len(candidates)):
        candidate_votes = 0
        percent = 0
        for j in range(len(votes)):
            if votes[j] == candidates[i]:
                candidate_votes = candidate_votes + 1
        # Store the vote for each candidate in vote_count list
        vote_count.append(candidate_votes)
        percent = (candidate_votes/total)
        percentage = f"{percent:.3%}"
        # Store the percentage of votes for each candidate in the vote_count list
        percentage_count.append(percentage)
    
    # Find the index for the winning candidate
    winner_id = vote_count.index(max(vote_count))

    # Print the results
    print("Election Results \n--------------------------------")
    print(f"Total Votes: {total}")
    print("--------------------------------")
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {percentage_count[i]} ({vote_count[i]})")
    print("--------------------------------")
    print(f"Winner: {candidates[winner_id]}")
    print("--------------------------------")

# Create an output file and store the results there
with open("Analysis/election_results.txt", "w") as f:
    print("Election Results \n--------------------------------", file = f)
    print(f"Total Votes: {total}", file = f)
    print("--------------------------------", file = f)
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {percentage_count[i]} ({vote_count[i]})", file = f)
    print("--------------------------------", file = f)
    print(f"Winner: {candidates[winner_id]}", file = f)
    print("--------------------------------", file = f)

