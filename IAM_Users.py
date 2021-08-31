import csv  # module for working with CSV files
import boto3 # module for AWS IAM python 
import json #module for json
import pprint 
from datetime import datetime
from datetime import date 



def IAM_Users(assume):

    pp = pprint.PrettyPrinter(indent=4)
        # telling boto3 script is using IAM service
    #client = boto3.client(        'iam',
    #    aws_access_key_id=assume['AccessKeyId'],
    #    aws_secret_access_key=assume['SecretAccessKey'],
    #    aws_session_token=assume['SessionToken']
    #)    # telling boto3 script is using IAM service

    client = boto3.client(        'iam', 
       aws_access_key_id=assume['AccessKeyId'],
       aws_secret_access_key=assume['SecretAccessKey'],
        aws_session_token=assume['SessionToken']
       
    )   

# List all users with the pagination interface
    paginator = client.get_paginator('list_users')
    for response in paginator.paginate():
        print(response)


    print('Start of User')

    pp.pprint(response)           
    print('hello')

    pp.pprint(response['Users'])

    Number_of_IAM_Users_only = "Number of IAM Users:" + " " + str(len(response['Users']))
    print(Number_of_IAM_Users_only)

    print("before")
    Number_of_IAM_Users = "List of IAM Users: "
    print(len(response['Users']))
    print(Number_of_IAM_Users)
    i = 0 
    while i < len(response['Users']):
        print(response['Users'][i]['UserName'])
        Number_of_IAM_Users +=  response['Users'][i]['UserName']
        Number_of_IAM_Users += ", "
        i += 1



    print(Number_of_IAM_Users, Number_of_IAM_Users_only)
    return Number_of_IAM_Users, Number_of_IAM_Users_only

