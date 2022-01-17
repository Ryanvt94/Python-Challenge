
#PyPoll
import os, csv

poll_path = os.path.join('..', r'PyPoll/Resources', 'pypoll_election_data.csv')

total_votes = 0
khan_vote = 0
correy_vote = 0
li_vote = 0
otooley_vote = 0

with open(poll_path) as pollfile:
    #read the file
    pollreader = csv.reader(pollfile, delimiter=',')
    header = next(pollreader)
    
    for row in pollreader:
        #total number of votes
        total_votes += 1

        #list of candidates that received votes
        if row[2] == "Khan":
            khan_vote += 1
        elif row[2] == "Correy":
            correy_vote += 1
        elif row[2] == "Li":
            li_vote += 1
        elif row[2] == "O'Tooley":
            otooley_vote += 1

#make a dictionary of candidate names and their votes
candidate_list = ["Khan", "Correy", "Li", "O'Tooley"]
candidate_votes = [khan_vote, correy_vote, li_vote, otooley_vote]

#find the winner
candidates_and_votes_dict = dict(zip(candidate_list,candidate_votes))
key = max(candidates_and_votes_dict, key=candidates_and_votes_dict.get)

#candidates votes by percent
khan_percent = (khan_vote/total_votes) * 100
correy_percent = (correy_vote/total_votes) * 100
li_percent = (li_vote/total_votes) * 100
otooley_percent = (otooley_vote/total_votes) * 100

#summary table
output = (
    f'Election Results\n'
    f'-----------------------\n'
    f'Total Votes: {total_votes}\n'
    f'-----------------------\n'
    f'Khan: {khan_percent:1,.2f}% ({khan_vote})\n'
    f'Correy: {correy_percent:1,.2f}% ({correy_vote})\n'
    f'Li: {li_percent:1,.2f}% ({li_vote})\n'
    f"O'Tooley: {otooley_percent:1,.2f}% ({otooley_vote})\n"
    f'-----------------------\n'
    f'Winner: {key}\n'
    f'-----------------------\n'
)
print(output)

#export file
output_file = os.path.join('..', 'PyPoll', 'Analysis/budget_analysis.txt')

with open(output_file, "w") as datafile:
    datafile.write(output)

