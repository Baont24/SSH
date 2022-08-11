from tracemalloc import start
import paramiko
import json

path_w = '/myfile.txt'

SeverTest = "172.25.3.123"

SeverTechX_32 = "172.20.1.32"
SeverTechX_33 = "172.20.1.33"


UserTechX = "ubuntu"
PassTechX = "SCIS7dkKqUWSRwWs9uQi"

Verify_OTP = "grep -i verifyAndSaveOtp.*{} containers/logs/rest-proxy-prod-3/application.log*"
log_tranID_OTP = "grep {} containers/logs/mas-rest-bridge-prod/application.log* -A 10"

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.load_system_host_keys()

ssh.connect(SeverTechX_33, port = 22, username = UserTechX, password = PassTechX)

accNumber = input("nhập số TK: ")

def Check_transID(accNumber):
    
    print('Running Check TransactionID')
    global transactionID
    (ssh_stdin, ssh_stdout, ssh_stderr) = ssh.exec_command(Verify_OTP.format(accNumber), get_pty = True)
    for line in ssh_stdout.readlines():
        print(line.rstrip())
        print(len(line.rstrip()))

        num_1 = line.find("transactionId") + 16
        num_2 = line.find("uri") - 3
        transactionID = line[num_1:num_2] 
    
    return transactionID


def Check_Log(accNumber):
    Trans_ID = Check_transID(accNumber)
    print('Running Check Log')
    (ssh_stdin, ssh_stdout, ssh_stderr) = ssh.exec_command(log_tranID_OTP.format(Trans_ID), get_pty = True)
    for line in ssh_stdout.readlines():
        print(line.rstrip())
        print("============================================================")
        
    # with open(output_file, "w+") as file:
    #     file.write(str(cmd_output))

Check_Log(accNumber)

    # cmd_output = ssh_stdout.read()
    # print('log printing: ', command, cmd_output)
    # # for line in ssh_stdout.readlines():
    # #     print(line.rstrip())

    # with open(output_file, "w+") as file:
    #     file.write(str(cmd_output))
        
    # return output_file