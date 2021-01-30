import socket

client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1",9999))

#data = "Hello"

file = open("Client.py", "r")
lines = file.readlines()
for data in lines:
	data = data.encode() #convert to binart form b'Hello'
	client_socket.send(data)

client_socket.close()
