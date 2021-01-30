import socket

client_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("192.168.90.99",9999))


'''
file = open("Client.py", "r")
lines = file.readlines()
for data in lines:
	data = data.encode() #convert to binart form b'Hello'
	client_socket.send(data)
'''

while True:
	data = input()
	data = data.encode()
	client_socket.send(data)
	data1 = client_socket.recv(1024)
	print("Data from server",data1.decode())

client_socket.close()
