#from threading import ExceptHookArgs
#from typing import Container
import boto3
import pprint 

pp = pprint.PrettyPrinter(indent=4)

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
response = client.describe_key_pairs(
    Filters=[
    ]
)
for instance in ec2.instances.all():
    print(
         "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
         instance.id, instance.platform, instance.instance_type, instance.public_ip_address, instance.image.id, instance.state
         )
     )
print("hello") 

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
#print(instances)




for instance in instances:
   print(instance.id, instance.instance_type)

for status in ec2.meta.client.describe_instance_status()['InstanceStatuses']:
   print(status)


print('before')
pp.pprint(response['KeyPairs'][0]["KeyName"])



print(len(response['KeyPairs']))


def list_EC2(assume):
    
    client = boto3.client(        'ec2',
        aws_access_key_id=assume['AccessKeyId'],
        aws_secret_access_key=assume['SecretAccessKey'],
        aws_session_token=assume['SessionToken']
    ) 
    response = client.describe_key_pairs(
    Filters=[
    ]
  
)
    
    example = {}
    
    i = 0 
    while i < len(response['KeyPairs']):
        print(response['KeyPairs'][i]["KeyName"])
        example[i] = response['KeyPairs'][i]["KeyName"]

        i += 1
    return example

#list_EC2()


response = client.describe_instances(
    Filters=[
      
    ],
    
    MaxResults=123,
   
)





example = {}

def EC2_insatances(assume):
#def EC2_insatances():
    
    client = boto3.client(        'ec2',
        aws_access_key_id=assume['AccessKeyId'],
        aws_secret_access_key=assume['SecretAccessKey'],
        aws_session_token=assume['SessionToken']
    ) 
    
    response = client.describe_instances(
        Filters=[
        ],
         MaxResults=123
    )
    i = 0
    # for testing 
    #print('before')
    #pp.pprint(response)
    #print('after')
    
    while i < len(response['Reservations']):
        print(response['Reservations'][i]['Instances'][0]['Tags'][0]['Value'])
        example[i] = response['Reservations'][i]['Instances'][0]['Tags'][0]['Value']
        i += 1
    return example



