import csv  # module for working with CSV files
import boto3 # module for AWS IAM python 
import json #module for json
import pprint 
from datetime import datetime
from datetime import date 
import pytz # module pytz
from datetime import datetime, timedelta




def check_role_used(assume):
######## start of actual program

    client = boto3.client(        'iam',
        aws_access_key_id=assume['AccessKeyId'],
        aws_secret_access_key=assume['SecretAccessKey'],
        aws_session_token=assume['SessionToken']
        )    # telling boto3 script is using IAM service

    print("start of program")

    
    d90 = datetime.today() - timedelta(days=90)
    d180 = datetime.today() - timedelta(days=180)
    d365 = datetime.today() - timedelta(days=365)

    #print(d180)

    local_tz = pytz.timezone('America/Los_Angeles')
    pastdate90 = local_tz.localize(d90, is_dst=None)
    pastdate180 = local_tz.localize(d180, is_dst=None)
    pastdate365 = local_tz.localize(d365, is_dst=None)
    # 2014-11-02 10:00:00 PST-0800

    #print(pastdate90)

    roles = client.list_roles(
        MaxItems=123
    )

    print('Number of roles')
    length = len(roles['Roles'])

    print(length)

# prints all the role names only 
    example = {}
    dict1 = {}
    i = 0
    while i < length:
        #print(roles['Roles'][i]['RoleName'])
    
        role_name_v = (roles['Roles'][i]['RoleName'])
    
        date_r = client.get_role(
            RoleName = role_name_v
        )
    
        
        

    # if statement to check if the role has ever been used 
        if date_r['Role']['RoleLastUsed'] == dict1:
            
            example[i] = roles['Roles'][i]['RoleName'],  "role never used"

            print(roles['Roles'][i]['RoleName'], "role never used")
        else:
            date_rr = (date_r['Role']['RoleLastUsed']['LastUsedDate'])
    
        

            if date_rr > pastdate90:
                example[i] = roles['Roles'][i]['RoleName'],  " used before 90 days"
                print(roles['Roles'][i]['RoleName'], " used before 90 days")
            elif date_rr < pastdate90:
                example[i] = roles['Roles'][i]['RoleName'],  " role not used before 90 days"
                print(roles['Roles'][i]['RoleName']," role not used before 90 days")
            elif date_rr < pastdate180:
                example[i] = roles['Roles'][i]['RoleName'], " role not used before 180 days"
                print(roles['Roles'][i]['RoleName']," role not used before 180 days")
            elif date_rr < pastdate365:
                example[i] = roles['Roles'][i]['RoleName'],  " role not used before 365 days"
                print(roles['Roles'][i]['RoleName']," role not used before 365 days")
    
        i += 1
    print(example)
    return example
# store all in list and then return list 

