import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Received")
s.bind(("localhost",2021)) #127.0.0.1
s.listen(3)

connection, client  = s.accept()
print(client, 'Connected :) ')
while True:
    data = connection.recv(32).decode()
    print("Received", data)
    if data=="!" :
        break

connection.close()