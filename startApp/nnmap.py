import socket
s = socket.socket()
s.connect(('127.0.0.1', 445))

s.send('Primal Security \n')

banner = s.recv(1024)
print(banner)