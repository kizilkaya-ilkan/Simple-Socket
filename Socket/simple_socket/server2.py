import socket

#socket oluştur
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "10.8.2.195"
port = 8080

#porta bind et
serversocket.bind((host, port))

# max 5 istek dinleme
serversocket.listen(1)
print("Listening...")

clientsocket,addr = serversocket.accept()
print("Baglanti alindi:" + str(addr))

while True:
	data = clientsocket.recv(1024)
	if not data:
		break
	clientsocket.sendall(data)

clientsocket.close()
