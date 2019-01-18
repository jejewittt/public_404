#!/usr/bin/env python3
import socket
import time

from multiprocessing  import Process





HOST = ""
PORT  = 8001
BUFFER_SIZE = 1024


def handle_echo(addr, conn):
	print("Connected by: ", addr)
	print(addr, conn)

	full_data = b""

	while True:
		data = conn.recv(BUFFER_SIZE)
		if not data: break 
		full_data+=data


	time.sleep(0.5) # dont have to have this 
	conn.sendall(full_data)
	conn.close()




def main():

	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		# s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

		s.bind((HOST, PORT))
		s.listen(2)


		# make the proxy into mupli proxy server as a challenge
		while True:
			conn, addr = s.accept()
			p = Process(target = handle_echo, args={addr,conn})
			p.daemon = True
			p.start
			print("strated process: ",p)
			# handle_echo(addr, conn)


	pass










if __name__ == "__main__":
	main()