from ast import Global
import socket
from tplinkcloud import TPLinkDeviceManager
import asyncio
import json
import os
from dotenv import load_dotenv

##KASA Connect
load_dotenv()
username = os.getenv("username")
password = os.getenv("password")

device_manager = TPLinkDeviceManager(username, password)

##Server Create
HOST = '' #socket.gethostname() #WLAN IPV4 Address, if it is blank string it will bind to server address
PORT = 6969 #Random port number
BUFFER_SIZE = 1024 #Max Size of Messages

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)##IPV4 and TCP 
server.bind((HOST,PORT))
server.listen(5)
print("Server Active")
print(f'Host: {HOST}')
print(f'Port: {PORT}')


######State of Plugs######
async def tapeState():
    device_name = "Tape (UCLA)"
    device = await device_manager.find_device(device_name)
    if device:
        my_dict = json.dumps(await device.get_sys_info(), indent=2, default=lambda x: vars(x)
                        if hasattr(x, "__dict__") else x.name if hasattr(x, "name") else None)
        my_dict = json.loads(my_dict)
        print(my_dict['relay_state'])
        return str(my_dict['relay_state'])
    else:  
        print(f'Could not find {device_name}')

async def noTapeState():
    global statenotape
    device_name = "No tape (UCLA)"
    device = await device_manager.find_device(device_name)
    if device:
        my_dict = json.dumps(await device.get_sys_info(), indent=2, default=lambda x: vars(x)
                        if hasattr(x, "__dict__") else x.name if hasattr(x, "name") else None)
        my_dict = json.loads(my_dict)
        print(my_dict["relay_state"])
        return str(my_dict['relay_state'])
    else:  
        print(f'Could not find {device_name}')

##########Tape Plug#######
#Toggle 
async def toggleTape():
    device_name = "Tape (UCLA)"
    device = await device_manager.find_device(device_name)
    if device:
        #print(f'Found {device.model_type.name} device: {device.get_alias()}')
        print(f'Toggling {device_name}')
        await device.toggle()
    else:  
        print(f'Could not find {device_name}')

#Turn on 
async def TurnOnTape():
    device_name = "Tape (UCLA)"
    device = await device_manager.find_device(device_name)
    if device:
        #print(f'Found {device.model_type.name} device: {device.get_alias()}')
        print(f'Turning On {device_name}')
        await device.power_on()
    else:  
        print(f'Could not find {device_name}')
#Turn off
async def TurnOffTape():
    device_name = "Tape (UCLA)"
    device = await device_manager.find_device(device_name)
    if device:
        #print(f'Found {device.model_type.name} device: {device.get_alias()}')
        print(f'Turning Off {device_name}')
        await device.power_off()
    else:  
        print(f'Could not find {device_name}')

###################No tape Plug##############
#Toggle 
async def toggleNoTape():
    device_name = "No tape (UCLA))"
    device = await device_manager.find_device(device_name)
    if device:
        #print(f'Found {device.model_type.name} device: {device.get_alias()}')
        print(f'Toggling {device_name}')
        await device.toggle()
    else:  
        print(f'Could not find {device_name}')

#Turn on 
async def TurnOnNoTape():
    device_name = "No tape (UCLA)"
    device = await device_manager.find_device(device_name)
    if device:
        #print(f'Found {device.model_type.name} device: {device.get_alias()}')
        print(f'Turning On {device_name}')
        await device.power_on()
    else:  
        print(f'Could not find {device_name}')
#Turn off
async def TurnOffNoTape():
    device_name = "No tape (UCLA)"
    device = await device_manager.find_device(device_name)
    if device:
        #print(f'Found {device.model_type.name} device: {device.get_alias()}')
        print(f'Turning Off {device_name}')
        await device.power_off()
    else:  
        print(f'Could not find {device_name}')


###Active Server
while True:
    clientsocket, address = server.accept()
    print(f'Connection from {address}')
    data_recv = clientsocket.recv(BUFFER_SIZE)
    print(f'Commanded to {data_recv}')

    if (data_recv == b'TapeState'):
        clientsocket.send(bytes(asyncio.run(tapeState()), "utf-8"))
    elif (data_recv == b'NoTapeState'):
        clientsocket.send(bytes(asyncio.run(noTapeState()), "utf-8"))
    
    elif (data_recv == b'TurnOnTape'):
        asyncio.run(TurnOnTape())
    elif (data_recv == b'TurnOffTape'):
        asyncio.run(TurnOffTape())
    
    elif (data_recv == b'TurnOnNoTape'):
        asyncio.run(TurnOnNoTape())
    elif (data_recv == b'TurnOffNoTape'):
        asyncio.run(TurnOffNoTape())
    else:
        clientsocket.send(bytes("A message was recived ", "utf-8"))

    clientsocket.close()