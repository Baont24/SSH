
import paramiko
import datetime

SeverDifi_1 = "172.20.1.32"
SeverDifi_2 = "172.20.1.33"

UserName = "ubuntu"
Password = "SCIS7dkKqUWSRwWs9uQi"

eqt_dofundtransfer = "grep eqt/dofundtransfer.*C{}1 containers/logs/mas-rest-bridge-prod/application.log*"

accNumber = input("Nhập số Sub ID: ")

def Check_TransID(accNumber):
    
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(SeverDifi_1, port = 22, username = UserName, password = Password)

    stdin, stdout, stderr = ssh.exec_command(eqt_dofundtransfer.format(accNumber))

    mesage = stdout.readlines()
    
    if mesage == []:
        print("Check Sever 33 - 32 None")
        ssh.connect(SeverDifi_2, port = 22, username = UserName, password = Password)
        stdin, stdout, stderr = ssh.exec_command(eqt_dofundtransfer.format(accNumber))
        for line in stdout.readlines():
            print(line.rstrip())
            
            num_1 = line.find("transactionId") + 16
            num_2 = line.find("uri") - 3
            transactionID = line[num_1:num_2]
        
            num_time1 = transactionID.find("-")
            num_time2 = int(transactionID[0:num_time1])
        
            times = str(datetime.datetime.utcfromtimestamp(num_time2 / 1e3))
            
            print("=================================")
            print(transactionID)
            print(times)
            
            print("============== 33 ===================")
        
            return transactionID
        
    else:
        print("Sever 32")
        stdin, stdout, stderr = ssh.exec_command(eqt_dofundtransfer.format(accNumber))
        for line in stdout.readlines():
            print(line.rstrip())
            
            num_1 = line.find("transactionId") + 16
            num_2 = line.find("uri") - 3
            transactionID = line[num_1:num_2]
            
            num_time1 = transactionID.find("-")
            num_time2 = int(transactionID[0:num_time1])
        
            times = str(datetime.datetime.utcfromtimestamp(num_time2 / 1e3))
            
            print("=================================")
            print(transactionID)
            print(times)
            
            print("============== 32 ===================")
            
            return transactionID

Check_TransID(accNumber)