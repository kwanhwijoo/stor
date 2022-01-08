import os
import multiprocessing
import time
import socket


print("Scanner running...")
start = time.time()


#검색할 IP주소 범위
baseIP = '10.30.160.'
#baseIP = '192.168.55.'
#시작 IP
startIP = 1
#마지막 IP
endIP = 254
#쓰레드 시작 간격
threadInterval=0 
#threadInterval=0.0005 #50ms

#ping 명령으로 IP 확인하는 함수
def checkIP(ip, queue):
  #print(ip)

  #IP주소로 한번만 ping을 보내 반응하는지 확인
  ret = os.system("ping -c 1 %s  2>&1 > /dev/null" %ip)
  if ret == 0:
    #print(ip + ': ok')
    #IP가 있으면 queue 에 해당 IP 추가
    queue.put(ip)


if __name__ == '__main__':
   m = multiprocessing.Manager()
  #multiprocessing용 큐
   queue = m.Queue()

   threadpool = []

   for ip in range(startIP, endIP):
    addr = baseIP+str(ip)
    #multiprocessing으로 쓰레드 생성
    p = multiprocessing.Process(target=checkIP, args=(addr,queue,))
    threadpool.append(p)

  #쓰레드 시작
   for th in threadpool:
    th.start()
    time.sleep(threadInterval)

  #모든 쓰레드가 종료될때 까지 대기
   for th in threadpool:
    th.join()
  #queue에 있는 IP주소 화면에 출력

   i = 0
   while queue.empty() == False:
    ip = queue.get(True)
    print(ip + ' is alive.')
    i+=1
    
   print(i)
   end = time.time()
   print('time elapsed:', end - start)
