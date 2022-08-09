from email import message
import paramiko

SeverDifi_1 = "172.20.1.32"
SeverDifi_2 = "172.20.1.33"

UserName = "ubuntu"
Password = "SCIS7dkKqUWSRwWs9uQi"

stockInfo = "grep eqt/stockInfo.*C{}*{} containers/logs/mas-rest-bridge-prod/application.log*"

accNumber = input("Nhập số Sub ID: ")
Stock = input("Nhập Mã CK: ")

def Check_TransID(accNumber, Stock):
    
    ssh = paramiko.SSHClient()

    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(SeverDifi_1, port = 22, username = UserName, password = Password)

    stdin, stdout, stderr = ssh.exec_command(stockInfo.format(accNumber, Stock))

    mesage = stdout.readlines()
    
    if mesage == []:
        print("Check Sever 33 - 32 None")
        ssh.connect(SeverDifi_2, port = 22, username = UserName, password = Password)
        stdin, stdout, stderr = ssh.exec_command(stockInfo.format(accNumber, Stock))
        for line in stdout.readlines():
            print(line.rstrip())
        print("============== 33 ===================")
        
    else:
        print("Sever 32")
        for line in stdout.readlines():
            print(line.rstrip())
        print("============== 32 ===================")

Check_TransID(accNumber, Stock)