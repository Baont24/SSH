from tabnanny import check
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
eqt_dofundtransfer = "grep eqt/dofundtransfer.*C{} containers/logs/mas-rest-bridge-prod/application.log*"

Tradex_market = "grep MONGO containers/share/app_env.sh"

log_tranID_OTP = "grep {} containers/logs/mas-rest-bridge-prod/application.log* -A 20"

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.load_system_host_keys()

ssh.connect(SeverTechX_33, port = 22, username = UserTechX, password = PassTechX)

transactionID = ""

def Check_transID():
    
    print('Running Check')
    global transactionID
    (ssh_stdin, ssh_stdout, ssh_stderr) = ssh.exec_command(Tradex_market, get_pty = True)
    for line in ssh_stdout.readlines():
        print(line.rstrip())

Check_transID()
