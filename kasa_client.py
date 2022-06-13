import socket

SERVER =  '45.79.102.78' # "DESKTOP-NF3N72J" "147.182.239.226" socket.gethostname()
PORT = 6969

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)##IPV4 and TCP 
# server.connect((SERVER, PORT))
# server.send(bytes("TurnOnTape", "utf-8"))
# server.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)##IPV4 and TCP 
server.connect((SERVER, PORT))
server.send(bytes("Sending messgae to see if connection", "utf-8"))
##server.send(bytes("TapeState", "utf-8"))
msg = server.recv(1024)
print(msg.decode("utf-8"))
server.close()