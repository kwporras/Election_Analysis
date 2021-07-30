# first python test
print("Hello World")
type(3)

#practice placing dictionaries with a list and manipulating the information
voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jeffersion", "registered_voters": 432438})
voting_data.insert(1, {"County": "El Paso", "registered_voters": 461149})
voting_data.remove({"county": "Arapahoe", "registered_voters":422829})
print(voting_data)
voting_data[2] = {"county": "Denver", "registered_voters": 463353}
voting_data[1] = {"county": "Jeffersion", "registered_voters": 432438}
voting_data.append({"county": "Arapahoe", "registered_voters": 422829})
print(voting_data)

#Practicing if statements
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

#Test of nested if-else statement

#What is the score?
score = int(input("What is your test score?"))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D')
            else:
                print('Your grade is an F.')


#Test if-elif-else statements

#What is the score?
score = int(input("What is your test score?"))

#Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is an B')
elif score >= 70:
    print('Your grade is an C')
elif score >= 60:
    print('Your grade is an D')
else:
    print('Your grade is an F.')


# Test membership Operators

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

# Test Logical Operators
# using "and"

if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

#using "or"
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")


# testing while loops
x = 0
While x <= 5:
    print(x)
    x = x + 1

# testing For loops
    # standard for loop
    counties = ["Arapahoe","Denver","Jefferson"]
    for county in counties:
        print(county)

    # iterate through list
    numbers = [0, 1, 2, 3, 4]
    for num in numbers:
        print(num)
    # iterate through list using range function
    for num in range(5):
        print(num)

    # iterate through list using i for Indexing
    for i in range(len(counties)):
            print(counties[i])
    
    # iterate through a dictionary
    # get both keys and and values
    counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

    for county in counties_dict:
        print(county)

    # get only keys
    for county in counties_dict.keys():
        print(county)

    print(counties_dict.keys())

    # get only values
    for voters in counties_dict.values():
        print(voters)

    #get values of a key
    for county in counties_dict:
        print(counties_dict.get(county))
    
    #get values and key for dictionary
    for key, value in counties_dict.items():
        print(key, value)
    
    for key, value in counties_dict.items():
        print(str(key) + " county has " + str(value) + " registered voters.")

    # iterate through a list of dictionaries(talk about)
    voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
    for county_dict in voting_data:
        print(county_dict)

    for county in range(len(voting_data)):

         print(voting_data[county]['county'])

    # get the values from a list of dictionaries
    for county_dict in voting_data:
        for value in county_dict.values():
            print(value)


# practice f-string and printing
    counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
    for county, voters in counties_dict.items():
        print(f'{county} county has {voters} registered voters.')     

#current problem
#dictionary
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                 {"county":"Denver", "registered_voters": 463353},
                 {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in range(len(voting_data)):
    print(f'{voting_data[county_dict]["county"]} county has {voting_data[county_dict]["registered_voters"]} registered voters.')


# test the dir() fuction

dir(int)
dir(float)
dir(bool)
dir(list)
dir(tuple)
dir(dict)
# may have to import first( these did not work)
import csv
dir(datetime)
dir(random)
dir(numpy)



# Practice reading files
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assing a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:


    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)
    
    # Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)






