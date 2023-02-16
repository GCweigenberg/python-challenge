import os
import csv

election_csv = os.path.join(".", "resources", "election_data.csv")

# count the total votes cast
total_votes_cast = 0
# list for the candidate names
candidates = []
# list of percentage of votes each candidate gets
candidate_percentages = []
# list for the number of votes each candidate gets
candidate_votes = []

with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        total_votes_cast = total_votes_cast + 1

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            candidate_votes.append(1)
        else:
            index = candidates.index(row[2])
            candidate_votes[index] += 1

    for votes in candidate_votes:
        percent = (votes/total_votes_cast) * 100
        percent = round(percent)
        percent = "%.3f%%" % percent
        candidate_percentages.append(percent)
    
    # determine winner
    x = max(candidate_votes)
    index = candidate_votes.index(x)
   

    winning_candidate = candidates[index]
    


# the results
print("Election Results")
print("----------------")
print(f"Total Votes: {str(total_votes_cast)}")
print("----------------")
for i in range(len(candidates)):
    print(
        f"{candidates[i]}: {str(candidate_percentages[i])} ({str(candidate_votes[i])})")
print(f"Winner: {winning_candidate}")


# export to .txt file
with open("Election Results.txt", "w") as text:
    text.write(f"Election Results\n")
    text.write(f"------------------------\n")
    text.write(f"Total Votes: {total_votes_cast}\n")
    text.write("-------------------------\n")
    for i in range(len(candidates)):
        text.write(
            f"{candidates[i]}: {str(candidate_percentages[i])} ({str(candidate_votes[i])})\n")
    text.write(f"Winner: {winning_candidate}")
