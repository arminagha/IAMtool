import csv  # module for working with CSV files
import boto3 # module for AWS IAM python 
import json #module for json
import pprint 
from datetime import datetime
from datetime import date 
import pytz # module pytz
from datetime import datetime, timedelta

pp = pprint.PrettyPrinter(indent=4)
def SAML_providers():
    client = boto3.client(        'iam',
        #aws_access_key_id=assume['AccessKeyId'],
        #aws_secret_access_key=assume['SecretAccessKey'],
        #aws_session_token=assume['SessionToken']
        )    # telling boto3 script is using IAM service
  

    client = boto3.client('iam',) 

    response = client.list_saml_providers()

    #pp.pprint(response['SAMLProviderList'])
    #pp.pprint(response)
    
    empty_list = {}
    dict = {}
    #if response['SAMLProviderList'] == empty_list:
    #    print("SAMLProviderList is empty")
    #    dict["sorry"] = "SAMLProviderList is empty"
    #elif response['SAMLProviderList'] != empty_list:
    #    print(response['SAMLProviderList'])

    #return dict

SAML_providers()