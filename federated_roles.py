
import csv  # module for working with CSV files
import boto3 # module for AWS IAM python 
import json #module for json
import pprint 
from datetime import datetime
from datetime import date 
import pytz # module pytz
from datetime import datetime, timedelta


def federated(assume):
    client = boto3.client(        'iam',
        aws_access_key_id=assume['AccessKeyId'],
        aws_secret_access_key=assume['SecretAccessKey'],
        aws_session_token=assume['SessionToken']
    )    # telling boto3 script is using IAM service
    pp = pprint.PrettyPrinter(indent=4)

    client = boto3.client('iam',) 


    response = client.list_roles(
 
    )

    pp.pprint("start")
    example = {}
    i = 0
    while i < len(response['Roles']):
        check_for_fed = response['Roles'][i]['AssumeRolePolicyDocument']['Statement'][0]['Principal']
    #print(check_for_fed) 

        key = 'Federated'
        if key in check_for_fed:
            example[i] = response['Roles'][i]['RoleName'],  "Federated key exist"
            print("In role: ",response['Roles'][i]['RoleName'], " Federated key exist")
    #else:
        #print("In role: ",response['Roles'][i]['RoleName'], "No Federated key exist")
          
        i += 1
    return example

