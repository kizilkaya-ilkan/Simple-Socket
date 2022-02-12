import socket

#socket oluştur
csocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "10.8.2.195"

port = 8080

#porta ve sunucuya bağlan

csocket.connect((host, port))

tm = csocket.recv(1024)

csocket.close()

print("Sunucuya baglanildi")
print(tm.decode('ascii'))
