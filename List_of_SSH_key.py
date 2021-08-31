
import csv  # module for working with CSV files
import boto3 # module for AWS IAM python 
import pprint 
import pytz # module pytz
from datetime import datetime, timedelta


def SSH_keypairs(assume):
    pp = pprint.PrettyPrinter(indent=4)

    client = boto3.client('iam',
        aws_access_key_id=assume['AccessKeyId'],
        aws_secret_access_key=assume['SecretAccessKey'],
        aws_session_token=assume['SessionToken']
    ) 
    example = {}
    # intizate dicnary to hold information
    paginator = client.get_paginator('list_users')
    for response in paginator.paginate():
        i = 0
        # while loop to cycle through users
        while i < len(response['Users']): 
            
            # print each user for clairty 
            pp.pprint(response['Users'][i]['UserName'])
            # set username to username variable
            iam_username = response['Users'][i]['UserName']

            shh = client.list_ssh_public_keys(
                UserName = iam_username 
                # input each user each cycle
            )

            x = 0
            while x < len(shh['SSHPublicKeys']): 
                print(shh['SSHPublicKeys'][i]['SSHPublicKeyId'])
                example[i] = "User: " +response['Users'][i]['UserName'] + " SSHPublicKeyId: " + shh['SSHPublicKeys'][i]['SSHPublicKeyId'] 

                x += 1
            i += 1

    return example