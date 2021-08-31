import csv  # module for working with CSV files
import boto3 # module for AWS IAM python 
import json #module for json
import pprint 
from datetime import datetime
from datetime import date 
import pprint 


now = datetime.now()    # gets the current date 
pp = pprint.PrettyPrinter(indent=4)

with open('datafile.txt', 'r') as csvfile:   # 
    rows = csv.reader(csvfile, delimiter=",")
    data = []

    for row in rows:
       print(row)


print("break")
reader = csv.reader(open('datafile.txt'))

result = {}
for row in reader:
    key = row[0]
    if key in result:
        # implement your duplicate row handling here
        pass
    result[key] = row[1:]

pp.pprint(result)
pp.pprint(result["account1"])

accountid = result["account1"]
