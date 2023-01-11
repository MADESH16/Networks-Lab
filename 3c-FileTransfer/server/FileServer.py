import socket
import sys

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',10000)
server.bind(server_address)
server.listen(1)
connection, client_address = server.accept()
filename = "sample.txt"
connection.sendall(filename.encode())
file=open("sample.txt","rb")

data=file.read()
connection.sendall(data)
file.close()
connection.close()
server.close()