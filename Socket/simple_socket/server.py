import socket
import time

#socket oluştur
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "10.8.2.195"

port = 8080

#porta bind et

serversocket.bind((host, port))

# max 5 istek dinleme
serversocket.listen(5)
print("Listening...%s")

while True:
	#bağlantı kur
	clientsocket,addr = serversocket.accept()
	
	print("Baglanti alindi: %s" % str(addr))
	currentTime = time.ctime(time.time()) + "\r\n"
	clientsocket.send(currentTime.encode('ascii'))
	clientsocket.close()
