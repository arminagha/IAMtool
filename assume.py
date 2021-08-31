import boto3
import botocore
import datetime
from dateutil.tz import tzlocal
from check_role_part2 import check_role_used

#assume-role  
# through csv 

# assume role in one account 

#response = client.assume_role(
#    RoleArn= 'arn:aws:iam::649834296163:role/admin_2',
#    RoleSessionName='admin_2_id_test'
    
#)

#print(response)


client = boto3.client('iam')      # telling boto3 script is using IAM service


def assume_role_client(account_Id, role_name):
  # config=botocore.client.Config(max_pool_connections=max_connections,retries=dict(max_attempts=max_attempts))
  
  print("assuming role in " + str(account_Id))
  stsclient=boto3.client('sts')
  assumed_role_object = stsclient.assume_role(
            RoleArn='arn:aws:iam::' + str(account_Id) + ':role/' + role_name,
            RoleSessionName="admin_2_id_test"+ str(account_Id)
        )
  print(assumed_role_object)
  credentials = assumed_role_object['Credentials'] 
  assumed_role_details = assumed_role_object['AssumedRoleUser']
  
  print("in")
  return credentials


client = boto3.client('iam',) 

#client = boto3.client(
#        'iam',
#        aws_access_key_id=assume['AccessKeyId'],
#        aws_secret_access_key=assume['SecretAccessKey'],
#        aws_session_token=assume['SessionToken']
#        )




if __name__ == "__main__":
    
  print("before")

  #test='admin'
  #assume_role_client(371377647465,test)

  #test='assume_role_'
  #assume = assume_role_client(649834296163,test)

  #check_role_used(assume)

  response = client.list_access_keys(
    #UserName='string',
    #Marker='string',
    #MaxItems=123
  )

  print(response)


  test='assume_role_'
  assume = assume_role_client(371377647465,test)
  check_role_used(assume)

  test='assume_role_'
  assume = assume_role_client(649834296163,test)
      #arn:aws:iam::649834296163:role/admin_2
    
  check_role_used(assume)
  
  test='Assume_role_'
  assume = assume_role_client(536930034755,test)
      #arn:aws:iam::649834296163:role/admin_2
    
  check_role_used(assume)




#assume_role_client(649834296163,test)
#check_role_90
#assume_role_client(649834296163,test)
#assume_role_client(649834296163,test)
#assume_role_client(649834296163,test)

#only account id will be changing 

#while i<len
#id_num
#assume_role_client(649834296163,test)


# mutiple accounts 

