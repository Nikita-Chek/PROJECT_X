import socket as st
import time
import threading
import sys
import os
sys.path.append(os.path.abspath('../RSA'))
import RSA

def recever(name, server, keys):
	try:
		while True:
			iTime = time.strftime('%m.%d--%M:%S', time.localtime())
			try:
				message = server.recv(2048)
				message = RSA.decryption(message, keys[0][0], keys[0][1])
				print(Fore.BLUE + iTime, 'Client: ', message)
			except:		
				conn.close()
			time.sleep(0.1)
	except:
		pass

def sender(conn, crypt):
	while True:
		try:
			message = input(Fore.GREEN)
			message = RSA.encryption(message,
									int(crypt[0]),
									int(crypt[1]))
			conn.send(message)
		except:
			print('client has been disconected')
			conn.close()
			server.listen(1)
			conn, addr = server.accept()
			print(addr, ' has connected')

#conection
host = st.gethostbyname(st.gethostname())
port = 9000
server = st.socket(st.AF_INET, st.SOCK_STREAM)
server.bind((host, port))
print('server started')
print('host IP: ', host, '\n')
server.listen(1)
conn, addr = server.accept()
print(addr, ' has connected')

#cryptographi
keys = RSA.key_generate()
mes = str(keys[1]).encode()
conn.send(mes)

crypt = conn.recv(2048).decode('utf-8')
crypt = crypt[1:-1].split(', ')


rT = threading.Thread(target = recever, args = ("recv_thread", conn, keys))
rT.start()

sender(conn, crypt)

rT.join()
server.close()