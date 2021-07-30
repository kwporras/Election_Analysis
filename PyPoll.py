# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Algorithm
# 1. Open the data file
# 2. Write down the dames of all the candidates
# 3. Add a voate count for each candidate
# 4. Get the total votes for each candidate
# 5. Get the total vaotes cast for the election



#How to see all functions available in the csv module
import csv
dir(csv)



#Read data from a file - direct path to the file

#Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

#Open the election results and read the file. (using Open() and close() formulas)
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()



#Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file. (using with formula )

with open(file_to_load) as elections_data:

    #to do: perform analysis.
    print(elections_data)



#Read data from a file - indirect path to the file

# see all the different attributes and methods that the os module uses
import os
print(dir(os))

#Allows access to files on different operating systems
os.path
dir(os.path)
#joins file path components together when they are provided as separate strings and returns with appropriate operatings system separator
#join()

#indirect path to file 
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Print the file object.
    print(elections_data)



# Create a filename variable to a direct or indirect path to the file.
import csv
import os
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file
open(file_to_save, "w")



# Test writing to txt file
# Create a filename variable to a direct or indirect path to the file. (using open() and close() formula)
import csv
import os
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()



# Test writing to txt file
# Create a filename variable to a direct or indirect path to the file. (using with formula)
import csv
import os
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    # txt_file.write("Hello World")
    # write additional data to the file.
    # txt_file.write("Arapahoe")
    # txt_file.write("Denver")
    # txt_file.write("Jefferson")
    # 1. Revise versions above to include space
    # txt_file.write("Arapahoe, ")
    # txt_file.write("Denver, ")
    # txt_file.write("Jefferson, ")
    # 2. Revise versions above to include space with one line of code
    # txt_file.write("Arapahoe, Denver, Jefferson")
    # 3. Revise versions above to write each county on separate lines (using newline escapte sequence ana \n)
    # Write three counties to the file.
    # txt_file.write("Arapahoe\nDenver\nJefferson")
    # Skill Drill
    txt_file.write("Counties in the Elections\n-------------------------\nArapahoe\nDenver\nJefferson")

#---------------------------------------------------------------------------------------------------------------#

# Begin 3.5.1 "Get the Total Votes"

import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save a file from a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")



#1. Initialize a total vote counter.
total_votes = 0

# Open the elction resutls and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)

        # 2. Add to the totol vote count.
        total_votes += 1
# 3. Print out the total votes.
print(total_votes)

#-----------------------------------------------------------------------------------
# Begin 3.5.2 Get the Candidates in the Election


import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save a file from a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize a new cadidate list.
candidate_options = []

# Open the elction resutls and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the totol vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)


# Print the candidate list.
print(candidate_options)

#---------------------------------------------------------------------------------------------------------

# 3.5.3 Get the Candidates' Votes & 
# 3.5.4 Determine Candidates' Percentage of Votes



import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save a file from a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Initialize a new cadidate list.
candidate_options = []
# Initialize a new cadidate dictionary
candidate_votes = {}

# Open the elction resutls and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the totol vote count.
        total_votes += 1

        # Print the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

        # Begin trackinging that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Print the candidate list.
print(candidate_options)

# Print the candidate vote dictionary
print(candidate_votes)


# Retrieve vote count of candidate.
for candidate_name in candidate_votes:

    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]   

    # Calculate the percentage of votes.
    votes_percentage = float(votes) / float(total_votes) * 100

    # Print the candidate name and perfecntage of votes.
    print(f"{candidate_name}: received {votes_percentage:.2f}% of the vote.")


#-------------------------------------------------------------------------------------

# 3.5.5 Determine the winning candidate

import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save a file from a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0
# Initialize a new cadidate list.
candidate_options = []
# Initialize a new cadidate dictionary
candidate_votes = {}
# Initialize Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the elction resutls and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the totol vote count.
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]

        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin trackinging that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Print the candidate list.
print(candidate_options)
# Print the candidate vote dictionary
print(candidate_votes)

# Retrieve vote count of candidate.
for candidate_name in candidate_votes:

    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]   
    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

    # Print the candidate name and percentage of votes (Skill challenege piece)
    #print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")

    # To do: print out each candidate's name, vote count, and perentage of votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # if true then set winning_count = votes and winning_percent = vote percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name

    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)




#------------------------------------------------------------------------------------------------------

# Module 3.6.1 Write the Election Results to a Text File

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate add it the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Save the fine vote count to the text file.
        txt_file.write(election_results)



    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the
        # terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)


        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidates' results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    # print(winning_candidate_summary)


#----------------------------------------------------------------------
#3.6.3 Writing the Winning Candidate's Results to a Text File

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)






