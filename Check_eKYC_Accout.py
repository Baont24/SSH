
import paramiko
import pandas
import datetime
import time

path_w = 'D:\Auto\SSH\ test.txt'

SeverDifi_1 = "172.20.1.32"
SeverDifi_2 = "172.20.1.33"

UserName = "ubuntu"
Password = "SCIS7dkKqUWSRwWs9uQi"

# Verify_OTP = "grep -i verifyAndSaveOtp.*{} containers/logs/rest-proxy-prod-3/application.log*"
# Verify_OTP_SMS = "grep {} containers/logs/notification-prod/application.log"
# grep -R PHONENUMBER containers/logs/notification-prod/*
# grep '/login.*stk' containers/logs/mas-rest-bridge-prod/application.log

eKYC_accout =  "grep '{}' containers/logs/ekyc-admin-prod/application.log"

Number_ID = input("Nhập số CCCD: ")

def Check_TransID(Number_ID):
    
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(SeverDifi_1, port = 22, username = UserName, password = Password)

    stdin, stdout, stderr = ssh.exec_command(eKYC_accout.format(Number_ID))

    mesage = stdout.readlines()
    
    if mesage == []:
        print("Check Sever 33 - 32 None")

        ssh.connect(SeverDifi_2, port = 22, username = UserName, password = Password)
        stdin, stdout, stderr = ssh.exec_command(eKYC_accout.format(Number_ID))
        for line in stdout.readlines():
            print(line.rstrip())

            print("=================================")
            
        print("============== 33 Done ===================")
                
    else:
        print("Sever 32")
  
        stdin, stdout, stderr = ssh.exec_command(eKYC_accout.format(Number_ID))
        for line in stdout.readlines():
            print(line.rstrip())
            
            print("=================================")
            
        print("============== 32 Done ===================")

Check_TransID(Number_ID)