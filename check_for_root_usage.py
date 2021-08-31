import boto3
import pprint 
pp = pprint.PrettyPrinter(indent=4)

client = boto3.client('iam')





#response = client.get_credential_report()
#pp.pprint(response['Content'])


client = boto3.client('cloudtrail')
response = client.list_trails(
    
)

pp.pprint(response['Trails'][0]['TrailARN'])
trailarn = response['Trails'][0]['TrailARN']
response = client.get_trail(
    Name = trailarn 
)

pp.pprint(response)
pp.pprint(response['Trail']['IsMultiRegionTrail'])

print('IsMultiRegionTrail: ' + str(response['Trail']['IsMultiRegionTrail']))