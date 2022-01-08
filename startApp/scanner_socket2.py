import os, sys
import ipaddress

used = []
notUsed = []
net = ''

def greet():
  print("Enter ipv4 network to check.  Format 192.168.5")
  global net
  net = input("Network > ")

def validate(i):
  v = i + '.1'
  ipaddress.ip_address(v)

def pingSweep(network):
  for i in range(1, 255):
    result = str.join('.', (net, str(i)))
    check(result)

def check(a):
  print("checking: %s" % a)
  if os.system("ping -c 1 %s 2>&1 > /dev/null" % a) == 0:
    used.append(a)
  else:
    notUsed.append(a)

def report():
  print("\nAddresses in use")
  print("*" * 20)
  for i in used:
    print(i)

  print("\nAddresses NOT in use")
  print("*" * 20)
  for i in notUsed:
    print(i)

def main():
  greet()
  validate(net)
  pingSweep(net)
  report()


if __name__ == '__main__':

  main()