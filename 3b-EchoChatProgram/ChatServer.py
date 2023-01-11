import socket
import sys
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',10000)

server.bind(server_address)
server.listen(1)
print("waiting for connection...")
connection, client_address = server.accept()
print("connection established with ",client_address)
message=""

while message!="end":
    data=connection.recv(1000).decode()
    if data:
        print(data)
        message=input()
        connection.sendall(message.encode())
    else:
        break

connection.close()
server.close()
