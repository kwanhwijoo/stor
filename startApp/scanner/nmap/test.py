import nmap
nm = nmap.PortScanner()
print(nm.scan('127.0.0.1', '22-443'))
