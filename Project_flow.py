import csv  #module for working with CSV files



# module - UI that says what CSV file to check 

# disply that your openning file

# open CSV file
with open('datafile.txt', 'r') as csvfile:   
    
    rows = csv.reader(csvfile, delimiter=",")
    data = []

    for row in rows:
       print(row)


# UI ask what infromation to check ? / or check everything

# API call to IAM pull infromation

# check infromation

# UI display if it follows or does not follow IAM best practices


# 