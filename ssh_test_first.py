import paramiko
import getpass
import time

print("SSH Client Start...\n")
start_time = time.time()


cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
 
# server = input("211.253.29.136")  # 호스트명이나 IP 주소
# user = input("root")  
# pwd = getpass.getpass("qwer43@!") # 암호입력 숨김
# server = input("Server: ")  # 호스트명이나 IP 주소
# user = input("Username: ")  
# pwd = getpass.getpass("Password: ") # 암호입력 숨김
# cli.connect(server, port=7777, username=user, password=pwd)

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










