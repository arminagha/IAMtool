import csv  # module for working with CSV files
import boto3 # module for AWS IAM python 
import json #module for json
import pprint 
from datetime import datetime
from datetime import date 


now = datetime.now()    # gets the current date 
pp = pprint.PrettyPrinter(indent=4)

with open('datafile.txt', 'r') as csvfile:   # 
    rows = csv.reader(csvfile, delimiter=",")
    data = []

    for row in rows:
       print(row)

client = boto3.client('iam')      # telling boto3 script is using IAM service


# line of code below creates IAM user named justanotheruser
#code   response = iam.create_user(UserName = 'justAnotherUser')

# List all users with the pagination interface
paginator = client.get_paginator('list_users')
for response in paginator.paginate():
    print(response)


print('hello')

# List only single user into with the pagination interface
response = client.get_user(
    UserName='armin'            # attach user to check

)



print(response)             # prints all infor for a single user
print('hello')
print(response['User']['UserName'])

Username = response['User']['UserName']     # stores the UserName value into Username variale
print('hello')

print(Username)

print('all info about roles')


roles = client.list_roles(
    
    #PathPrefix='RoleName',
    #Marker='RoleName',
    MaxItems=123
)



pp.pprint(roles)
print('List of roles')
print(roles['Roles'][0]['RoleName'])
print(roles['Roles'][1]['RoleName'])
print(roles['Roles'][2]['RoleName'])
print(roles['Roles'][3]['RoleName'])

print('Number of roles')
length = len(roles['Roles'])

print(length)

# prints all the role names only 
i = 0
while i < length:
    print(roles['Roles'][i]['RoleName'])
    i += 1


# loop through list 


date_r = client.get_role(
    RoleName='Admin'
)

pp.pprint(date_r)
print('all info about roles')
pp.pprint(date_r['Role']['RoleLastUsed']['LastUsedDate'])
print(type(date_r['Role']['RoleLastUsed']['LastUsedDate']))

date_rr = date_r['Role']['RoleLastUsed']['LastUsedDate']
print("hererererereeeeeeeeee")
print(date_rr)

year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
print(year,month,day)



only_date = date_rr.date()
print(only_date)

current_date = year + "-" + month + "-" + day
print(current_date)


import datetime
import pytz

now = datetime.datetime.now()
# here, now.tzinfo is None, it's a naive datetime
now = pytz.utc.localize(now)

print(type(now))

print(type(date_rr))



print(now)



print(date_rr)



if now > date_rr:
  print("now is Greater")
if date_rr > now:
  print("date_rr is Greater")


start_date = datetime.datetime.now() - datetime.timedelta(30)
from datetime import datetime, timedelta
    
d90 = datetime.today() - timedelta(days=90)
d180 = datetime.today() - timedelta(days=180)
d365 = datetime.today() - timedelta(days=365)


print(start_date)
print(d180)

import pytz # module pytz

local_tz = pytz.timezone('America/Los_Angeles')
pastdate90 = local_tz.localize(d90, is_dst=None)
pastdate180 = local_tz.localize(d180, is_dst=None)
pastdate365 = local_tz.localize(d365, is_dst=None)
# 2014-11-02 10:00:00 PST-0800

print(pastdate90)


# checks if last time they logged in was before 30 days
if pastdate90 > date_rr:
  print("pastdate is Greater")
if date_rr > pastdate90:
  print("date_rr is Greater")

if date_rr > pastdate90:
    print("role used before 90 days")
elif date_rr < pastdate180:
    print("role not used before 180 days")
elif date_rr > pastdate180:
    print("role used before 180 days")









######## start of actual program

print("start of program")
from datetime import datetime, timedelta
    
d90 = datetime.today() - timedelta(days=90)
d180 = datetime.today() - timedelta(days=180)
d365 = datetime.today() - timedelta(days=365)


print(start_date)
print(d180)

import pytz # module pytz

local_tz = pytz.timezone('America/Los_Angeles')
pastdate90 = local_tz.localize(d90, is_dst=None)
pastdate180 = local_tz.localize(d180, is_dst=None)
pastdate365 = local_tz.localize(d365, is_dst=None)
# 2014-11-02 10:00:00 PST-0800

print(pastdate90)



roles = client.list_roles(
    MaxItems=123
)

print('Number of roles')
length = len(roles['Roles'])

print(length)



# prints all the role names only 
i = 0
while i < length:
    #print(roles['Roles'][i]['RoleName'])
    
    role_name_v = (roles['Roles'][i]['RoleName'])
    
    date_r = client.get_role(
        RoleName = role_name_v
    )
    #pp.pprint(date_r)
    

    dict1 = {}

    # if statement to check if the role has ever been used 
    if date_r['Role']['RoleLastUsed'] == dict1:
        print(roles['Roles'][i]['RoleName'], "role never used")
    else:
        date_rr = (date_r['Role']['RoleLastUsed']['LastUsedDate'])
    
        #print(date_rr)

        if date_rr > pastdate90:
            print(roles['Roles'][i]['RoleName']," used before 90 days")
        elif date_rr < pastdate90:
            print(roles['Roles'][i]['RoleName']," role not used before 90 days")
        elif date_rr < pastdate180:
            print(roles['Roles'][i]['RoleName']," role not used before 180 days")
        elif date_rr < pastdate365:
            print(roles['Roles'][i]['RoleName']," role used before 365 days")

    
    
    i += 1







#   problem right now the role has never been used 



# prints all the role names only 
#i = 0
#while i < length:
   # role_name = (roles['Roles'][i]['RoleName'])
    
   # date_r = client.get_role(
   # RoleName= role_name
   # )
   # print(role_name)
   # date_rr = date_r['Role']['RoleLastUsed']['LastUsedDate']    # date the role was last used
    



   # i += 1


# loop through list 







