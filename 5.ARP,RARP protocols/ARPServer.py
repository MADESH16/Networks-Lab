import socket

table={
    '192.168.1.1':'1E.4A.4A.11',
    '192.168.1.2':'7E.5A.4A.11',
    '192.168.1.3':'4E.4A.4A.11',
    '192.168.4.1':'3E.2A.4A.11',
    '192.168.5.1':'7E.2A.4A.11',
}

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',1234))
s.listen()

clientsocket,address=s.accept()

print("Connection From" ,address,"Has Established")
ip=clientsocket.recv(1024)
ip=ip.decode("utf-8")
mac=table.get(ip,'No entry for given address')
clientsocket.send(mac.encode())