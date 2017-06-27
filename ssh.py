"""
    Application that demonstrates establishing an SSH connection with a linux server to displaying
    specific information about the server (version, disk-usage, memory-usage, etc.)
"""
import paramiko

print("Opening SSH session.")

# here, paramiko establishes the SSH connection with our linux server
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect("IP_OF_SERVER", username="HOST_NAME", password="HOST_PASSWORD")

# our three commands that are used to display the information desired on the linux server
COMMAND_LIST = ['uname -a', 'df -h', 'cat /proc/meminfo']

# iterates through the list of commands that we have and executes them
for i in range(len(COMMAND_LIST)):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(COMMAND_LIST[i])
    print(str(ssh_stdout.read(), 'utf-8'))

# always remember to close your open ssh sessions.
ssh.close()

print("SSH session closed.")