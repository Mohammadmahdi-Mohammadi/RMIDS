import socket

s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s1.bind(("localhost",2021)) #127.0.0.1
#s2.bind(("localhost",2022)) #127.0.0.1

#bool check1 = False
#check2 = False
client2 = 0
s1.listen(2)
#s2.listen(2)

#print("here: ", s.accept())
connection1, client1  = s1.accept()
#connection2, client2  = s2.accept()

if client1 != "" and client2 == "":
    print(client1, 'first port Connected :) ')
    check1 = True
    while True:
        data = connection1.recv(32).decode()
        print("Received", data)
        if data == "!":
            break

    connection1.close()

elif client1 == "": #and client2 != "":
    print(client2, 'second port Connected :) ')
    check2 = True
    while True:
        data = connection2.recv(32).decode()
        print("Received", data)
        if data == "!":
            break
    connection2.close()

else:
    #client1 == "" and client2 = "":
    print(" medium is get into trouble")

    connection2.close()





#s.listen(3)
#if(s.accept() != )
#connection1, client1  = s.accept()


