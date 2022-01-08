#Nmap을 사용한 포트 스캐너(결과를 실행화면에 출력)

import nmap

nm = nmap.PortScanner()
result = nm.scan(hosts="127.0.0.1",ports='20-443', arguments='-sV')

for host in nm.all_hosts():
    print('-------------------------------------------------')
    print('Host : %s (%s)' %(host, nm[host].hostnames()))
    print('State : %s' % nm[host].state())
    proto = 'tcp'
    print('--------')
    print('Protocol : %s' %proto)
    lport = nm[host][proto].keys()
    for port in sorted(lport):
        print ('port : %s\tstate : %s' % (port,str(nm[host][proto][port]['state'])))