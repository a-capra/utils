import paramiko

username = "acapra"
hostname = "lxplus.cern.ch"
password = "xxxxxxxxxxxx"
port = 22

command = "./vnc.cmd"

try:
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy)
    
    client.connect(hostname, port=port, username=username, password=password)

    stdin, stdout, stderr = client.exec_command(command)

    print(stdout.read().decode('utf-8'))

finally:
    client.close()