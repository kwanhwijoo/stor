import socket
import ipaddress
import re

port_regex = re.compile("([0-9]+){1,5}-([0-9]+){1,5}")
ip_regex1 = re.compile("^\d")
ip_regex2 = re.compile("^www\.")

while True:
    ip_addr_input = input("IP주소 또는 도메인 주소를 입력하세요(ex: 127.0.0.1 or www.naver.com) :")
    try:
        ip_regex1_valid = ip_regex1.search(ip_addr_input.replace(" ",""))
        ip_regex2_valid = ip_regex2.search(ip_addr_input.replace(" ",""))
        if ip_regex1_valid:
            ip_addr = ipaddress.ip_address(ip_addr_input)
            break
        elif ip_regex2_valid: 
            ip_addr = ip_addr_input
            break
    except:
        print("잘못된 주소 형식입니다.")

while True:
    port_min = 0
    port_max = 65535
    port_range = input("포트범위를 정해주세요(ex:0-65535) :")
    port_range_valid = port_regex.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

valid_ports = []
for port in range(port_min, port_max + 1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.4)
            s.connect((ip_addr, port))
            valid_ports.append(port)

    except:
        # print("port",port,"not open")
        pass

for port in valid_ports:
    print(f"{ip_addr_input} 주소에 {port}가 연결되었습니다")