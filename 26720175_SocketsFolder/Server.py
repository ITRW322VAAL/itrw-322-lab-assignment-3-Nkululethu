import socket

Host ='127.0.01'  //STANDARD LOOPBACK INTERFACE ADDRESS (LOCAL HOST)
PORT= 9999        //PORT to listen on

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
	s.bind((HOST,PORT))
	s.listen()
	conn, addr = s.accept()
	with conn:
		print('Server is connected with address', addr)
		while True:
			data = conn.recv(2048)     //default byte stream size
			if not data:
				break
			conn.sendall(data)