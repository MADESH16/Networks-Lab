import socket

hostname=socket.gethostname()
ipaddr="localhost"
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr=(ipaddr,1234)
c="Y"
while c.upper() == "Y":
    req_domain=input("Enter domain name for which the IP is needed : ")
    send=s.sendto(req_domain.encode(),addr)
    data,address=s.recvfrom(1024)
    reply_ip=data.decode().strip()
    print(f"The ip for the domain name {req_domain} is {reply_ip}")
    c=(input("Continue? (y/n)"))

s.close()