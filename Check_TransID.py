import paramiko
import pandas
import datetime
import time

path_w = 'D:\Auto\SSH\ test.txt'

SeverDifi_1 = "172.20.1.32"
SeverDifi_2 = "172.20.1.33"

UserName = "ubuntu"
Password = "SCIS7dkKqUWSRwWs9uQi"

log_tranID = "grep {} containers/logs/mas-rest-bridge-prod/application.log* -A 20"

accNumber = input("Nhập TransID: ")

transactionID = ""

def Check_TransID(accNumber):
    
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(SeverDifi_1, port = 22, username = UserName, password = Password)

    stdin, stdout, stderr = ssh.exec_command(log_tranID.format(accNumber))

    mesage = stdout.readlines()
    
    if mesage == []:
        print("Check Sever 33 - 32 None")
        ssh.connect(SeverDifi_2, port = 22, username = UserName, password = Password)
        stdin, stdout, stderr = ssh.exec_command(log_tranID.format(accNumber))
        for line in stdout.readlines():
            print(line.rstrip())

            print("====================================")
        print("================= 33 Done ===================")
        
    else:
        print("Sever 32")
        stdin, stdout, stderr = ssh.exec_command(log_tranID.format(accNumber))
        for line in stdout.readlines():
            print(line.rstrip())

            print("====================================")
        print("================ 32 Done ===================")

Check_TransID(accNumber)