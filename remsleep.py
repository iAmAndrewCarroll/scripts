import paramiko
from dotenv import load_dotenv
import os

# env variables
load_dotenv()

# fetch variables
password = os.getenv("PASSWORD")
hostname = os.getenv("HOST")
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

  # execute sleep
  stdin, stdout, stderr = ssh.exec_command("sudo shutdown now")

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
  print(f"An error occurred: {str(e)}")