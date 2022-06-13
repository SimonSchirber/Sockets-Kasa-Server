import socket 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)##IPV4 and TCP 
server.connect(('172.28.107.66', 6969))

server.send(bytes(" request state", "utf-8"))
msg = server.recv(1024)
print(msg.decode("utf-8"))