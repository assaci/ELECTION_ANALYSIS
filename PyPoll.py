# The data we need to retrieve.
# Import teh datetime class from the datetime module.
import datetime
import csv
import os
from stat import FILE_ATTRIBUTE_READONLY
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save teh file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# open teh election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

     
# Close the file 

# 1. The total number of votes cast 
# 2. A complete list of candidates who received votes 
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of election based on popular vote.