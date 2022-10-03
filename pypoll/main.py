#Imports for working with CSV Files
import os
import csv

#Path to CSV
poll_report_csv = os.path.join("Resources", "election_data.csv")

#Global Variables
#List for holding Candidate names
tank = []
#Dictonary for holding candidate names and vote totals
vote_dict = {}


#Open the CSV file
with open(poll_report_csv) as poll_csv:
    pollcsvreader = csv.reader(poll_csv, delimiter=",")
    #Skip the column headers
    pollcsvheader = next(pollcsvreader)
    
    #The only column in the CSV file that we will need to work with is row[2]. We can derive the candidate's 
    #names and their vote counts from this column. The following places row[2] in the Cand_Name variable.
    for row in pollcsvreader:
        Cand_Name = (row[2])

        #-----MAKING A DICTIONARY-----
        #A dictionary with the candidate name as a key and the vote count as a value will be created with this data.
        #The first step is to get the unique candidate names. This is done by appending the candidate name to the
        #tank list if that name is not found in tank list. This will give us 3 unique values.
        if Cand_Name not in tank:
            tank.append(Cand_Name)
            #Creating a value of 0 for each key in the vote_dict dictionary.
            vote_dict[Cand_Name] = 0 
        #As python is running the loop 1 is added to the value for the appropriate key.
        vote_dict[Cand_Name] += 1
        #The vote_dict dictionary:
        # {'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}
        #-----------------------------

    #This returns the total votes by summing the values in vote_dict.
    bignum = sum(vote_dict.values())
    #This returns the maximum value in vote_dict. This is used to declare a winner.
    winning_num = max(vote_dict.values())
    #Use a list comprehension to return the key for winning_num variable.
    winner = {i for i in vote_dict if vote_dict[i]== winning_num}
    
    #Print Statements
    print("Election Results")
    print("============================================")
    print(f"Total Votes:  {bignum}")
    print("============================================")
    #The following loop uses the libary items() function
    for key, value in vote_dict.items():
        #The items are then printed along with text for all values and keys in the library
        #This gives us the "block" of candidates, vote percentages and vote counts in our terminal and text file.
        print(key," | Percentage:", round((int(value)/int(bignum))*100,3),"| Raw Votes:", value, )
    print("============================================")
    #Removes the curly brackets and the single quotes from the beginning and end of the winner variable
    #to closer match the format of the other print statements.
    print(f"Winner:  {str(winner)[2:-2]}")
    print(vote_dict)
    
    #Export to a text file
with open('Analysis/pypoll.txt', 'w') as f:
    f.write("Election Results")
    f.write("\n")
    f.write("============================================")
    f.write("\n")
    f.write(f"Total Votes:  {bignum}")
    f.write("\n")
    f.write("============================================")
    f.write("\n")
    for key, value in vote_dict.items():
        f.write(f"{key} | Percentage: {round((int(value)/int(bignum))*100,3)} | Raw Votes:{value}")
        f.write("\n")
    winner = {i for i in vote_dict if vote_dict[i]== winning_num}
    f.write("============================================")
    f.write("\n")
    f.write(f"Winner:  {str(winner)[2:-2]}")


        



       

