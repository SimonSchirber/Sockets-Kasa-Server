import socket

HOST = socket.gethostname() #WLAN IPV4 Address
PORT = 6969 #Random port number

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)##IPV4 and TCP 
server.bind((HOST,PORT))

BUFFER_SIZE = 1024

##up to how may devices can listen
server.listen(5)
print("Server Active")
print(f'Host: {HOST}')
print(f'Port: {PORT}')

while True:
    clientsocket, address = server.accept()
    print(f'Connection from " {address} " has been established')
    data_recv = clientsocket.recv(BUFFER_SIZE)
    print(f'Data recieved is {data_recv}')
    clientsocket.send(bytes("you are recieving server packets", "utf-8"))
    clientsocket.close()


