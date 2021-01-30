import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binding 
server_socket.bind(("127.0.0.1", 9999))
server_socket.listen()
#wait for client
print("wait for client")
client_socket, addr = server_socket.accept()#blocking call
#print("client connected", client_socket) #info of the data



while True:
	data = client_socket.recv(1024)
	if (data):
		data = data.decode()
		print("Data From Client", data)
	else:
		break

server_socket.close()
