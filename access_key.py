import csv  # module for working with CSV files
import boto3 # module for AWS IAM python 
import json #module for json
import pprint 
from datetime import datetime
from datetime import date 
import pytz # module pytz
from datetime import datetime, timedelta



def access_key(assume):
  client = boto3.client(        'iam',
        aws_access_key_id=assume['AccessKeyId'],
        aws_secret_access_key=assume['SecretAccessKey'],
        aws_session_token=assume['SessionToken']
    )    # telling boto3 script is using IAM service

  d90 = datetime.today() - timedelta(days=90)
  d180 = datetime.today() - timedelta(days=180)
  d365 = datetime.today() - timedelta(days=365)

    #print(d180)

  local_tz = pytz.timezone('America/Los_Angeles')
  pastdate90 = local_tz.localize(d90, is_dst=None)
  pastdate180 = local_tz.localize(d180, is_dst=None)
  pastdate365 = local_tz.localize(d365, is_dst=None)

  pp = pprint.PrettyPrinter(indent=4)

  client = boto3.client('iam') 

  paginator = client.get_paginator('list_users')
  for response in paginator.paginate():
    print(response)


  print('Start of User')

  pp.pprint(response)           
  print('hello')

  pp.pprint(response['Users'])
  pp.pprint(response['Users'][0])
  pp.pprint(response['Users'][0]['UserName'])
  pp.pprint(response['Users'][1]['UserName'])

  print(len(response['Users']))
  example = {}
  y = 0
  i = 0
  while i < 3:
    username = response['Users'][i]['UserName']

    list_access_key = client.list_access_keys(
      UserName = username

    )
    print("Name of User ", username)
    x = 0
    while x < len(list_access_key['AccessKeyMetadata']):
      create_date = list_access_key['AccessKeyMetadata'][x]['CreateDate']

      if create_date > pastdate90:
        print(list_access_key['AccessKeyMetadata'][x]['AccessKeyId']," was rotated before 90 days")
        example[y]  = list_access_key['AccessKeyMetadata'][x]['AccessKeyId']," was rotated before 90 days"
      elif create_date < pastdate90:
        print(list_access_key['AccessKeyMetadata'][x]['AccessKeyId']," was not rotated before 90 days")
        example[y]  = list_access_key['AccessKeyMetadata'][x]['AccessKeyId']," was not rotated before 90 days"
      elif create_date < pastdate180:
        print(list_access_key['AccessKeyMetadata'][x]['AccessKeyId']," was not rotated before 180 days")
        example[y] = list_access_key['AccessKeyMetadata'][x]['AccessKeyId']," was not rotated before 180 days"
      elif create_date < pastdate365:
        print(list_access_key['AccessKeyMetadata'][x]['AccessKeyId']," was not rotated before 365 days")
        example[y] = list_access_key['AccessKeyMetadata'][x]['AccessKeyId']," was not rotated before 365 days"
      x += 1
      y += 1


    i += 1

  return example
















