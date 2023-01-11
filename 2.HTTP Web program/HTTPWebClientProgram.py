import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("google.com",80))
s.sendall(b"GET/HTTP/1.1\r\nHost:www.google.com\r\nAccept:text/html\r\n\r\n")
print(str(s.recv(4096),'utf-8'))

