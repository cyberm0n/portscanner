import socket

banner = r"""  _________                    ____  ___
 /   _____/ ____ _____    ____ \   \/  /
 \_____  \_/ ___\\__  \  /    \ \     / 
 /        \  \___ / __ \|   |  \/     \ 
/_______  /\___  >____  /___|  /___/\  \
        \/     \/     \/     \/      \_/   0.4v

"""

print(banner)

host = input("host > ").strip().lower()
portx = int(input("port range > ")) +1

open_ports = []
s = socket.socket()

def scan(host,port):
	try:
		s.connect((host, port))
	except:
		pass
	else:
		open_ports.append(port)

for i in range(1,portx):
	scan(host,i)

print("Open Ports:")
if len(open_ports) != 0:
	for i in open_ports:
		print(i)
else:
	pass
