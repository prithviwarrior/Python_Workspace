import socket
import threading

#thread to handle communication with client
def client_handler(client_socket):
	
	
	while True:
		data = client_socket.recv(1024)
		if (data != "exit"):
			data = data.decode()
			print("Data From Client", data)
			client_socket.send(input().encode())
			client_socket.send(data.upper().encode())
		else:
			break
	client_socket.close()

#main thread
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binding 
server_socket.bind(("192.168.91.156", 9999))
server_socket.listen()
#wait for client

while True:
	print("wait for client")
	client_socket, addr = server_socket.accept()#blocking call
	th1 = threading.Thread(target = client_handler, args=(client_socket,))
	th1.start()


server_socket.close()
