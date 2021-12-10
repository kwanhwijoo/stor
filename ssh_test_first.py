import paramiko
import getpass
import time

print("SSH Client Start...\n")
start_time = time.time()


cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
 

cli.connect("xxx", port=xxx, username="xxxx", password="xxxx")

# stdin, stdout, stderr = cli.exec_command("c")
# stdin, stdout, stderr = cli.exec_command("ls -al")

stdin, stdout, stderr = cli.exec_command("uname -a")
lines = stdout.readlines()
# print(''.join(lines))


# sftp = cli.open_sftp()
# stdin, stdout, stderr = sftp.put("test.txt", "/tmp/test.txt")
# lines = stderr.readlines()

cli.close()
end_time = time.time()
print("WorkingTime: {} sec".format(end_time-start_time))


# split_lines = lines.split() 

for str in lines:
    split_lines = str.split(" ")
    print(split_lines[0])
    print(split_lines[1])










