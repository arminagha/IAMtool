import boto3
import pprint 
pp = pprint.PrettyPrinter(indent=4)


def active_password1234(assume):
  client = boto3.client('iam',
    aws_access_key_id=assume['AccessKeyId'],
    aws_secret_access_key=assume['SecretAccessKey'],
    aws_session_token=assume['SessionToken'])

  response = client.list_users()

  #pp.pprint(response['Users'])

  example = {}
  x = 0
  while x < len(response['Users']):
    dic_check = response['Users'][x]
    key_to_lookup = 'PasswordLastUsed'
    if key_to_lookup in dic_check:
      print("Active Password in: " + response['Users'][x]['UserName'])
      example[x]  = "Active Password in: " + response['Users'][x]['UserName']
      
    x +=1 

  return example

#active_password()