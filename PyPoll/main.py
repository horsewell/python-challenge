# Modules
import os
import csv

# Set path for file
csvpath = os.path.join(".", "Resources", "election_data.csv")
txtpath = os.path.join(".", "analysis", "election_analysis.txt")

# declare variables
total_votes = 0
candidates  = []
count_votes = []
count_max   = 0
winner      = ""

output = []

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # store the header
    header_row = next(csv_reader)   

    for row in csv_reader:
        # count all votes
        total_votes += 1

        # if new candidate not in the candidates list add and add 1 vote to corrosponding count_votes position
        if row[2] not in candidates:
            candidates.append(row[2])
            count_votes.append(1)
        else:
            # if candidate already in candidates just increase the votes
            count_votes[candidates.index(row[2])] += 1
        
# Create Output

output.append(f"Election Results")
output.append(f"-------------------------")
output.append(f"Total Votes: {total_votes}")
output.append(f"-------------------------")
# cycle through the candidates
for candidate in candidates:
    candidate_votes = count_votes[candidates.index(candidate)]
    output.append(f"{candidate}: {candidate_votes/total_votes:.3%} ({candidate_votes})")
    # get the maximum votes for the candidate
    if candidate_votes > count_max:
        count_max = candidate_votes
# the winner is the one with the max votes
winner = candidates[count_votes.index(count_max)]
output.append(f"-------------------------")
output.append(f"Winner: {winner}")
output.append(f"-------------------------")

# save and print output

print(*output, sep = "\n")
with open(txtpath, 'w', encoding='UTF-8') as f:
    f.writelines('\n'.join(output))
