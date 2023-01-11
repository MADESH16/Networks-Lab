import socket

dns_table={"www.google.com":"192.165.1.1","www.youtube.com":"192.165.1.2","www.fb.com":"192.165.1.3","www.amazon.com":"192.165.1.4"}
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

print("Starting server.....")

s.bind(("127.0.0.1",10000))
while True:
    data,address = s.recvfrom(4096)
    print(f"{address} wants to fetch data")
    data=data.decode()
    ip=dns_table.get(data,"Not Found!").encode("utf-8") 
    send=s.sendto(ip,address)

    