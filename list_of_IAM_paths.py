import boto3
from collections import Counter
import pprint 

pp = pprint.PrettyPrinter(indent=4)

client = boto3.client('iam')

response = client.list_roles(
    MaxItems=123
)



#pp.pprint(response['Roles'][0]['Path'])
#pp.pprint(response['Roles'][0]['RoleName'])

#print(len(response['Roles']))


example = {}
only_values = {}

def IAM_paths(assume):
    
    client = boto3.client('iam',
        aws_access_key_id=assume['AccessKeyId'],
        aws_secret_access_key=assume['SecretAccessKey'],
        aws_session_token=assume['SessionToken']
    ) 
    
    response = client.list_roles(
        MaxItems=123
    )
   
    i = 0
    
    while i < len(response['Roles']):
    #while i < 1:    
        #pp.pprint("Role:" + response['Roles'][i]['RoleName'] + " Path: " +response['Roles'][i]['Path'])
        example[i] = "Role:" + response['Roles'][i]['RoleName'] + " Path: " +response['Roles'][i]['Path']
        only_values[i] = response['Roles'][i]['Path']
      
        #example[i+1] = response['Roles'][i]['RoleName']
        i += 1
    pp.pprint(only_values)

    res = Counter(only_values.values())

    #pp.pprint(res)
    #newvalues = (str(only_values).replace(', ',',\n '))
    #newres = (str(res).replace(', ',',\n '))

    #print(newvalues)      
    #print(newres)

   
    return example, res


#pp.pprint(example)


#IAM_paths()