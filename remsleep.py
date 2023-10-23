import paramiko
from dotenv import load_dotenv
import os

# env variables
load_dotenv()

# fetch variables
password = os.getenv("PASSWORD")
hostname = os.getenv("CHONK_IP")
print(f"Hostname: {hostname}")

port = 22 # default port for SSH
username = "andrew"
print(f"username: {username}")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
  # Connect to the remote
  ssh.connect(hostname, port, username, password)
  print("SSH connection successful")

  # execute sleep wiht provided password
  command = f"echo '{password}' | sudo -S shutdown now"
  stdin, stdout, stderr = ssh.exec_command(command)

  # Display output
  print(stdout.read().decode())

  # Display errors, if any
  print(stderr.read().decode())

  # terminate connection
  ssh.close()

  print(f"{hostname} is sleeping soundly")
except paramiko.AuthenticationException:
  print("Please check your credentials.")
except paramiko.SSHException as e:
  print(f"SSH connection failed: {str(e)}")
except Exception as e:
  pass # print(f"An error occurred: {str(e)}")