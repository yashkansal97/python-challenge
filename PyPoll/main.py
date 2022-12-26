import os
import csv

polls = os.path.join('Resources','election_data.csv')

with open(polls) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)

    votes = []

    for row in csv_reader:
        votes.append(row[2])
    
    total = len(votes)

    candidates = list(set(votes))
    vote_count = []
    percentage_count = []

    for i in range(len(candidates)):
        candidate_votes = 0
        percent = 0
        for j in range(len(votes)):
            if votes[j] == candidates[i]:
                candidate_votes = candidate_votes + 1
        vote_count.append(candidate_votes)
        percent = (candidate_votes/total)
        percentage = f"{percent:.3%}"
        percentage_count.append(percentage)


    print("Election Results \n--------------------------------")
    print(f"Total Votes: {total}")
    print("--------------------------------")
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {percentage_count[i]} ({vote_count[i]})")
    
    winner_id = vote_count.index(max(vote_count))
    print("--------------------------------")
    print(f"Winner: {candidates[winner_id]}")
    print("--------------------------------")

