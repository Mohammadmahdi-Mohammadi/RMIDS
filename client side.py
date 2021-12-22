import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("localhost",2021)) #127.0.0.1

while True:
    msg = input()
    if msg == "~":
        break
    try:
        s.send(msg.encode())
    except:
        print("Connection Lost!")
        break

s.close()

