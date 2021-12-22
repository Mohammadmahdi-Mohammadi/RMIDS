import socket

clientsocket = socket.socket()

host = "127.0.0.1"
port = 10000


print("waiting for connections")
try:
    clientsocket.connect((host,port))
except socket.error as e:
    print(str(e))

Response = clientsocket.recv(1024)
print(Response.decode("utf-8"))
while True:
    Input = input("say something")
    clientsocket.send(str.encode(Input))
    response = clientsocket.recv(1024)
    print((response.decode("utf-8")))
