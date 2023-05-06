import threading
import socket

ADDR="14:5a:fc:3e:c3:9e" # Clients MAC ADDRESS
FORMAT="utf-8"
DISCONNECT_MESSAGE="!DISCONNECT"

server=socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
server.bind((ADDR, 4)) # Where 4 is CHANNEL
server.listen(1)

client, addr=server.accept()

try:
    while True:
        data=client.recv(1024)
        if not data:
            break
        print("Message: {}".format(data.decode(FORMAT)))
        message=input("Enter Message:")
        client.send(message.encode(FORMAT))
except OSError as e:
    pass

client.close()
server.close()

