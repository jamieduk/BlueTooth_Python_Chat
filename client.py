import socket
import time

ADDR="14:5a:fc:3e:c3:9e" # Servers MAC ADDRESS
FORMAT="utf-8"
DISCONNECT_MESSAGE="!DISCONNECT"

client=socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

client.connect((ADDR, 4)) # Where 4 is CHANNEL

try:
    while True:
        message=input("Enter Message: ")
        client.send(message.encode("utf-8"))
        data=client.recv(1024)
        if not data:
            break
        print("Message: {}".format(data.decode('utf-8')))
except OSError as e:
    pass
    
client.close()

