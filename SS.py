import socket
from _thread import *
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# _____________________________________________________________
# network configuration
host = socket.gethostname()
port = 10000
ThreadCount = 0
r_array =  ["Ford", "Volvo", "BMW"]

class university:
    def __init__(self):

        self.country = "Iran"
        self.city = "Tehran"
        self.address = "No. 350, Hafez Ave, Valiasr Square"
        self.name = "Amirkabir University of Technology"
        self.contact_array =  {"tel" : "+98(21)66419506" , "fax" : "+98(21)66495519" , "email" : "pheeaut.ac.ir"}

    def contact_Info(self):
        return self.contact_array
    def phone(self):
        print(self.address)
        return self.country

# _____________________________________________________________

AUT = university()
AUT.phone()


# When an error occurs, or exception as we call it,
# Python will normally stop and generate an error message.
try:
    serversocket.bind((host,port))
# except socket.error as e:
# print(str(e))
except:
    print("Sth Went wrong during binding! ")

# _____________________________________________________________

print("Waiting for connection an client .... ")
serversocket.listen(5)
# the argument to listen tells the socket library that we want it to queue up
# as many as 5 connect requests (the normal max) before refusing outside connections.
# If the rest of the code is written properly, that should be plenty
# Ref: https://docs.python.org/3/howto/sockets.html

print("??1??")
def client_thread(connection):
    print("??2??")
    connection.send(str.encode("Welcome to the server"))
    while True:
        # print("Array value is: ", r_array[0])
        data = connection.recv(2048)
        print("recievd method:  ", data.decode("UTF-8"))
        data = data.decode("UTF-8")
        temp = ""
        temp = exec(data)
        print("temp value is: ", temp)


        r_array[0] = data;
        # reply = "Hello I'm the server" + data.decode("utf-8")
        if not data:
            break
        #   [socket.send] ->  is a low-level method and basically just the C/syscall method send(3) / send(2).
        #                     It can send less bytes than you requested, but returns the number of bytes sent.

        # **** [socket.sendall]   -> is a high-level Python-only method that sends the entire buffer you pass or throws an exception.
        #                        It does that by calling socket.send until everything has been sent or an error occurs.
        connection.sendall(str.encode(temp))
    connection.close()
print("??3??")

while True:
    # print("??4??")
    # print(serversocket.accept())
    print("??4??")
    # if not serversocket.accept():
    #     print("threre isn't anyone!")

    client,address = serversocket.accept()
    print("here is client: ",  client)
    print("here is ip: " ,  address)
    print("connected to " + address[0] +"   " + str(address[1]))

    # -------------------------------------------------------------------------------------------
    # _thread.start_new_thread(function, args[, kwargs])
    # ------> Start a new thread and return its identifier. The thread executes the function
    #         function with the argument list args (which must be a tuple). The optional kwargs
    #         argument specifies a dictionary of keyword arguments.
    #         When the function returns, the thread silently exits.
    start_new_thread(client_thread , (client,))
    ThreadCount += 1
    # -------------------------------------------------------------------------------------------


    print("Threadnumber" + str(ThreadCount))
socketserver.close()