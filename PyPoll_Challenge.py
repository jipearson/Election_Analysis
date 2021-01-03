# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options/candidate votes
candidate_options = []
candidate_votes = {}

#county_options/county_votes
county_options = []
county_votes = {}

# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Track the county with the highest turnout count
county_highest_turnout = ""
county_turnout_count = 0 

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
        county_name = row[1]
        
        # If the candidate does not match any existing candidate add it the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # If the county does not match any existing county add it the county list.
        if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)
            # And begin tracking that county's voter count.
            county_votes[county_name] = 0
        # Add a vote to that county's count
        county_votes[county_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for county_name in county_votes:
        # Retrieve vote count and percentage.
        votes_county = county_votes[county_name]
        vote_percentage = float(votes_county) / float(total_votes) * 100

        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes_county:,})\n")
        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        #  Save the county results to our text file.
        txt_file.write(county_results)  

        # Determine the county with the largest turnout.
        if (votes_county > county_turnout_count):
            county_turnout_count = votes_county
            county_highest_turnout = county_name   

    largest_county_turnout_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {county_highest_turnout}\n"
    #    f"Winning Vote Count: {county_turnout_count:,}\n"
        f"-------------------------\n")

    print(largest_county_turnout_summary)
    # Save the winning candidate's results 

    txt_file.write(largest_county_turnout_summary)

    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

        candidate_results = (
            f"\n{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
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
        f"\n-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)

    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
