import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
#1.Initialize a total vote counter
total_votes = 0
# Using the open() function with the "w" mode we will write data to the file.
candidate_options = []

#Declare an empty dictionary.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
     #To do: read and analyze the data here
     file_reader = csv.reader(election_data)
     #Read the header row
     headers = next(file_reader)
     #prin each row in the CSV file
     for row in file_reader:
          #2. Add to the total vote count.
          total_votes += 1
          #Print the candidate name from each row.
          # Candidate column is the third column
          # that has the second index, so we would use,
          # row[2] to reference the Candidate column.
          candidate_name = row[2]
          # Add the candidate name to the candidate list.
          if candidate_name not in candidate_options:
               #Add it to the list of candidates
               candidate_options.append(candidate_name)

               candidate_votes[candidate_name] = 0
                # 2. Begin tracking that candidate's vote count.
                # Add a vote to that candidate's count.
          candidate_votes[candidate_name] += 1

     for candidate_name in candidate_votes:
           # 2. Retrieve vote count of a candidate.
          votes = candidate_votes[candidate_name]
          # 3. Calculate the percentage of votes.
          vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
          # print(f"{candidate_name}: received {vote_percentage}% of the vote.")
          # Determine winning vote count and candidate
# 1. Determine if the votes are greater than the winning count.  
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               # 2. If true then set winning_count = votes and winning_percent =
               # vote_percentage.
               winning_count = votes
               winning_percentage = vote_percentage
               # 3. Set the winning_candidate equal to the candidate's name.
               winning_candidate = candidate_name
          print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
     winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
#3 Print the total votes
#print(total_votes)
#3 Print the total votes
#If the candidate does not match any existing candidate...
# To do: print out each candidate's name, vote count, and percentage of
# votes to the terminal.


     
          #add it to the list of candidates.

#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote
# Create a filename variable to a direct or indirect path to the file.