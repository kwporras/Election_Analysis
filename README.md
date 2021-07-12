# Election_Analysis

## Overview of Election Audit
The Colorado election committee asked for a number of analytical metrics to be automated in python. If so, they would like to apply it to other congressional districts, senatorial districts, and local elections. In addition to the automation of code and analytical metrics, a request for suggestions for future coding adjustments have been requested.

##### The requested analytical metrics are listed below:
1. Total votes cast
2. Total votes per candidate
3. Percentage of votes per candidate
4. Voter turnout per county
5. Percentage of total votes per county
6. County with the highest turnout
7. Winner of election based on the popular vote



## [Election-Audit Results](Analysis/election_analysis.txt)
### The analysis of the election shows that:

- The total votes were 369,711
- The number and percentage of total votes for each county in the precinct were:
  - Jefferson: 10.5% (38,855)
  - Denver: 82.8% (306,055)
  - Arapahoe: 6.7% (24,801)
- The county with the largest county turnout was Denver
- The number of votes and percentage of total votes for each candidate received were:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
- The winner of the election was:
  - Winner: Diana DeGette
  - Winning Vote Count: 272,892
  - Winning Percentage: 73.8%


## Election-Audit Summary
The script below is used to define how data in a readable csv will be indexed. In the future if a csv file is provided the candidate name or county name may not be in the same columns as csv file in the [resources file](Resources/election_results.csv). By changing the row index the script can be adjust to correctly read a different csv column layout.        
![alt text](https://github.com/kwporras/Challenge-3/blob/f84a76aac82899721c48edec85bfddcd5d698444/Resources/Create_a_variable_to_track.PNG)

Additionally, if another variable in a CSV file that needs to be tracked, the below script provides a general useable outline. Use the script above create a new row index, then place that index in the "Insert index number here" spot. Then county_list and county_votes would be replaced and appropriated named for the data that one would wish to track.  
![alt text](https://github.com/kwporras/Challenge-3/blob/f84a76aac82899721c48edec85bfddcd5d698444/Resources/Selection_of_county_and_candidate_data.PNG)

##### Resources
- Data Source: election_results.csv
- Software: Python 3.9.6, Visual Studio Code, 1.58.0





