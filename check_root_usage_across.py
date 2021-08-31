import boto3 # module for AWS IAM python 
import pprint 

pp = pprint.PrettyPrinter(indent=4)
client = boto3.client('iam') 



response = client.get_account_password_policy()


pp.pprint(response)