import socket as st
import threading
import time
import sys
import os
sys.path.append(os.path.abspath('../RSA'))
import RSA
import registration as r

def recever(name, keys):
	try:
		while True:
			iTime = time.strftime('%m.%d--%H:%M', time.localtime())
			try:
				message = server.recv(2048)
				message = RSA.decryption(message, keys[0][0], keys[0][1])
				print(iTime, 'Server: ', message)
			except:
				break
			time.sleep(0.1)
	except:
		pass

def sender(crypt):
	while True:
		try:
			message = input()
			message = RSA.encryption(message,
									int(crypt[0]),
									int(crypt[1]))
			server.send(message)
		except:
			break

#login
name = r.main()
print(name)
#conection
server = st.socket(st.AF_INET, st.SOCK_STREAM)
host = input(str('host IP: '))
#host = st.gethostbyname(st.gethostname())
port = 9000
server.connect((host, port))

#cryptographi
crypt = server.recv(2048).decode('utf-8')
crypt = crypt[1:-1].split(', ')

keys = RSA.key_generate()
mes = str(keys[1]).encode()
server.send(mes)

rT = threading.Thread(target = recever, args = ("recv_thread", keys))
rT.start()

sender(crypt)

rT.join()
