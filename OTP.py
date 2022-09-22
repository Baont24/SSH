
import paramiko
import pandas
import datetime
import time

path_w = 'D:\Auto\SSH\ test.txt'

SeverDifi_1 = "172.20.1.32"
SeverDifi_2 = "172.20.1.33"

UserName = "ubuntu"
Password = "SCIS7dkKqUWSRwWs9uQi"

Verify_OTP = "grep -i verifyAndSaveOtp.*{} containers/logs/rest-proxy-prod-3/application.log*"
# Verify_OTP_sms = "grep {} containers/logs/notification-prod/application.log"

accNumber = input("Nhập số TK: ")

transactionID = ""

def Check_TransID(accNumber):
    
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(SeverDifi_1, port = 22, username = UserName, password = Password)

    stdin, stdout, stderr = ssh.exec_command(Verify_OTP.format(accNumber))

    mesage = stdout.readlines()
    
    if mesage == []:
        print("Check Sever 33 - 32 None")

        ssh.connect(SeverDifi_2, port = 22, username = UserName, password = Password)
        stdin, stdout, stderr = ssh.exec_command(Verify_OTP.format(accNumber))
        for line in stdout.readlines():
            print(line.rstrip())
            num_1 = line.find("transactionId") + 16
            num_2 = line.find("uri") - 3
            transactionID = line[num_1:num_2]
            
            num_time1 = transactionID.find("-")
            num_time2 = int(transactionID[0:num_time1])
        
            times = str(datetime.datetime.utcfromtimestamp(num_time2 / 1e3))
            
            print(times)
            print(transactionID)
            
            f = open(path_w, "w")
            f.write(times)
            f.write("--")
            f.write(transactionID)
            
            print("============== 33 Done ===================")
            
            return transactionID
        
    else:
        print("Sever 32")
  
        stdin, stdout, stderr = ssh.exec_command(Verify_OTP.format(accNumber))
        for line in stdout.readlines():
            print(line.rstrip())
            num_1 = line.find("transactionId") + 16
            num_2 = line.find("uri") - 3
            
            transactionID = line[num_1:num_2]
    
            num_time1 = transactionID.find("-")
            num_time2 = int(transactionID[0:num_time1])
            times = str(datetime.datetime.utcfromtimestamp(num_time2 / 1e3))
            
            print(num_time2)
            print(transactionID)
            
            print("============== 32 Done ===================")
            
            return transactionID

Check_TransID(accNumber)