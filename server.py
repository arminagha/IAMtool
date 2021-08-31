from flask import Flask, render_template, request
import boto3
import botocore
import datetime
from dateutil.tz import tzlocal
from check_role_part2 import check_role_used
from federated_roles import federated
from List_of_SAML_providers import SAML_providers
from IAM_Users import IAM_Users
from access_key import access_key
from VPC_endpoints import VPC_endpoints
from List_EC2 import list_EC2, EC2_insatances
from list_of_IAM_paths import IAM_paths
from List_of_SSH_key import SSH_keypairs
from active_password import active_password1234

import csv
app = Flask(__name__)

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







@app.route('/data', methods=['GET','POST'] )
def data():
  if request.method == 'POST':
    f = request.form['csvfile']
    data = []
    with open(f) as file:
      csvfile = csv.reader(file)
      #print(data[0][0])
    
      for row in csvfile:
        data.append(row)
        #print(data)
        #print(data[0][2][0])
      print("after")
      print(data)
      print("numbers")
      print(data[1])
      print("numbers")
      print(data[1][0])
      accid = []
      acc = []
      accid = data.pop()
      acc = data.pop()
      print(accid)
      print(acc)
      
      # test for check role accounts
      for x in range(len(accid)):
        print(accid[x])
        accound_id = accid[x]
        test = 'admin_2'
        assume = assume_role_client(accound_id,test)
        test = check_role_used(assume)
        with open( str(accound_id) +' checkrole.txt', 'w') as f:
          f.writelines(str(test))
      
      # test for federated roles
      for x in range(len(accid)):
        accound_id = accid[x]
        test = 'admin_2'
        assume = assume_role_client(accound_id,test)
        test = federated(assume)
        with open( str(accound_id) +' federated_roles.txt', 'w') as f:
          f.writelines(str(test))


      # test for access keys
      for x in range(len(accid)):
        accound_id = accid[x]
        test = 'admin_2'
        assume = assume_role_client(accound_id,test)
        test = access_key(assume)
        with open( str(accound_id) +' Access_keys.txt', 'w') as f:
          f.writelines(str(test))

      # test for VPC_endpoints
      for x in range(len(accid)):
        accound_id = accid[x]
        test = 'admin_2'
        assume = assume_role_client(accound_id,test)
        #arn:aws:iam::649834296163:role/admin_2
        test = VPC_endpoints(assume)
        with open( str(accound_id) +' VPC_Endpoints.txt', 'w', newline='') as f:
          f.writelines(str(test))
          
        # test for IAM Users
      for x in range(len(accid)):
        accound_id = accid[x]
        test = 'admin_2'
        assume = assume_role_client(accound_id,test)
        test = IAM_Users(assume)
        with open( str(accound_id) +' IAM_Users.txt', 'w', newline='') as f:
          f.writelines(str(test))
           

        # test List EC2 keypairs
      for x in range(len(accid)):
        accound_id = accid[x]
        test = 'admin_2'
        assume = assume_role_client(accound_id,test)
        test = list_EC2(assume)
        with open( str(accound_id) +' List_EC2_keypairs.txt', 'w', newline='') as f:
          f.writelines(str(test))


         # test List EC2 instances
      for x in range(len(accid)):
        accound_id = accid[x]
        test = 'admin_2'
        assume = assume_role_client(accound_id,test)
        test = EC2_insatances(assume)
        with open( str(accound_id) +' List_EC2_instances.txt', 'w', newline='') as f:
          f.writelines(str(test))

      # test for IAM Paths
      for x in range(len(accid)):
        accound_id = accid[x]
        test = 'admin_2'
        assume = assume_role_client(accound_id,test)
        test = IAM_paths(assume)
        with open( str(accound_id) +' IAM_paths.txt', 'w', newline='') as f:
          f.writelines(str(test))
     
      # test for IAM SSH key pairs
      for x in range(len(accid)):
        accound_id = accid[x]
        test = 'admin_2'
        assume = assume_role_client(accound_id,test)
        test = SSH_keypairs(assume)
        with open( str(accound_id) +' SSHkeypairs.txt', 'w', newline='') as f:
          f.writelines(str(test))

       # test for Active passwords
      for x in range(len(accid)):
        accound_id = accid[x]
        test = 'admin_2'
        assume = assume_role_client(accound_id,test)
        test = active_password1234(assume)
        with open( str(accound_id) +' active_password.txt', 'w', newline='') as f:
          f.writelines(str(test))

         # test for SAML providers
      #for x in range(len(accid)):
      #  accound_id = accid[x]
      #  test = 'admin_2'
      #  assume = active_password(accound_id,test)
      #  test = SSH_keypairs(assume)
      #  with open( str(accound_id) +' SAML providers.txt', 'w', newline='') as f:
      #    f.writelines(str(test))



    return render_template('data.html', accid=accid)  






@app.route('/', methods=['GET','POST'])
def index():



  return render_template('index.html')





@app.route('/my-link/')
def my_link():
  print ('I got clicked!')
  test='Assume_role_'
  # test = admin_2
  assume = assume_role_client(536930034755,test)
      #arn:aws:iam::649834296163:role/admin_2
    
  test = check_role_used(assume)
  return  test


@app.route('/SAML_providers/')
def SAML_providers():
  test='Assume_role_'
  assume = assume_role_client(536930034755,test)
      #arn:aws:iam::649834296163:role/admin_2
    
  test = SAML_providers(assume)
  
  return  test


@app.route('/checkrole/')
def checkrole():
  print ('I got clicked!')
  test='admin_2'
  #assume = assume_role_client(536930034755,test)
  assume = assume_role_client(649834296163,test)
  #649834296163
      #arn:aws:iam::649834296163:role/admin_2
  accountID = 536930034755  
  test = check_role_used(assume)
 #lines = ['Readme', 'How to write text files in Python']
  with open( str(accountID) +'checkrole.txt', 'w') as f:
    f.writelines(str(test))
    f.write('\n')
  return  test

@app.route('/checkIAMUsers/')
def checkIAMUsers():
  
  #test='Assume_role_'
  #assume = assume_role_client(536930034755,test)
      #arn:aws:iam::649834296163:role/admin_2
    
  #test = IAM_Users(assume)
  test = IAM_Users()
  return  test


#Federated
@app.route('/federated/')
def Federated():
  
  test='Assume_role_'
  assume = assume_role_client(536930034755,test)
      #arn:aws:iam::649834296163:role/admin_2
    
  test = federated(assume)
  return  test








@app.route('/hugetest/', methods=['GET','POST'])
def hugetest():
  f = request.form['csvfile']
  data_1 = []
  with open(f) as file:
    csvfile = csv.reader(file)
      #print(data[0][0])
    
    for row in csvfile:
      data_1.append(row)
        #print(data)
        #print(data[0][2][0])
    print("after")
    print(data_1)
    print("number0968708s")
    print(data_1[1])
    print("numbers onlylyyyy")
    print(data_1[1][1])
    accid = []
    acc = []
    accid = data_1.pop()
    acc = data_1.pop()
    print(accid)
    print(acc)
    i = 0
  while i < len(accid):
    test='Assume_role_'
    assume = assume_role_client(accid,test)
      #arn:aws:iam::649834296163:role/admin_2
     
    test = check_role_used(assume)
 #lines = ['Readme', 'How to write text files in Python']
    with open( str(accid) +'checkrole.txt', 'w') as f:
      f.writelines(str(test))
      f.write('\n')
  return  test





if __name__ == '__main__':
  app.run(debug=True)
  #app.run(host="44.197.214.38", port=8080)
  #44.197.214.38