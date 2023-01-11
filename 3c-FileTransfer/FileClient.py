import socket
import sys

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address=('localhost',10000)
client.connect(server_address)

filename=client.recv(1000).decode()
filename="hello"+filename
file=open(filename,"wb")
data=client.recv(4097)

file.write(data)
file.close()
client.close()
