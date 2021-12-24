# --------------------------------------------------------------

# https://stackoverflow.com/questions/3906232/python-get-the-print-output-in-an-exec-statement
# Since Python 3.4 there is a solution is the stdlib:
import time
import sys
from io import StringIO
import contextlib

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old
    #
    # with stdoutIO() as s:
    #     exec(data)
    #
    # print("out:", s.getvalue())
# --------------------------------------------------------------

import socket
from _thread import *
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# _____________________________________________________________
# network configuration
host = socket.gethostname()
port = 10000
ThreadCount = 0
r_array =  ["Ford", "Volvo", "BMW"]


#------------------------------------------------------------------------------
# class university:
#     def __init__(self):
#
#         self.country = "Iran"
#         self.city = "Tehran"
#         self.address = "No. 350, Hafez Ave, Valiasr Square"
#         self.name = "Amirkabir University of Technology"
#         self.contact_array =  {"tel" : "+98(21)66419506" , "fax" : "+98(21)66495519" , "email" : "pheeaut.ac.ir"}
#
#     def contact_Info(self):
#         return self.contact_array
#     def phone(self):
#         print(self.address)
#         return self.country

class Library:
    def __init__(self, listofbooks):
        self.availablebooks = listofbooks


    def displayAvailablebooks(self):
        print("The books we have in our library are as follows:")
        print("====================================================== ")
        send_data = "The books we have in our library are as follows:@======================================================  "
        for book in self.availablebooks:
            print(book)
            send_data = send_data +"@ " + book[0] + " | " + book[1]
        return send_data

    def addBook(self, student):
        # print("hhhhhhhhhhhhh")
        student_array = student.get_array()
        # print("hhhhhhhhhhhhhggggggg")
        if len(student_array) > 0:
            # print("hhhhhhh23452hhhhhhggggggg")
            # print("List of books you have borrowed: ")
            index = 1
            for book in student_array:
                print(index, "- ", book)
                index += 1
            print("Enter the desired book number in range of 1 to ", index - 1, " : ")
            booknum = input()
            while (int(booknum) > index - 1 or int(booknum) < 0):
                print("Enter the desired book number in range of 1 to ", index - 1, " : ")
                booknum = input()
            add_index = int(booknum) - 1
            self.availablebooks.append((student_array[add_index]))
            student.del_b_book(int(booknum) - 1)
            print("Thanks for returning your borrowed book")
        else:
            print(" \n \n----------------------------------------------------------------------- \n "
                  "You have not borrowed any books from the library \n"
                  " and therefore it is not possible to provide services to you in this section :\  \n"
                  "-----------------------------------------------------------------------")

    def lendBook(self, requestedBook, requestedBook_author, student_array):
        if (requestedBook, requestedBook_author) in self.availablebooks:
            print("The book you requested has now been borrowed")
            pm = "The book you requested has now been borrowed"
            self.availablebooks.remove((requestedBook, requestedBook_author))
            student_array.append((requestedBook, requestedBook_author))
        else:
            print("Sorry the book you have requested is currently not in the library")
            pm = "Sorry the book you have requested is currently not in the library"
        return pm


class Student:
    Borrowed_list = []

    def get_array(self):
        return self.Borrowed_list

    def del_b_book(self, index):
        del self.Borrowed_list[index]

    def requestBook(self):
        print("Enter the name of the book you'd like to borrow: ")
        self.book = input()
        print("Enter the name of the author: ")
        self.author = input()
        return self.book, self.author

    def returnBook(self):
        print("Enter the name of the book you'd like to return>>")
        self.book = input()
        return self.book





# _____________________________________________________________

# AUT = university()
# AUT.phone()

library = Library([("The Soul of a New Machine", "Tracy Kidder"),
                       ("Software and Hardware Problems and Solutions", "Simon Monk"),
                       ("Fundamentals of Superscalar Processors", "John Shen"),
                       ("Structured Computer Organization", "Andrew Tanenbaum"),
                       ("Computer Networking: A Top Down Approach", "James Kurose"),
                       ("Computer Architecture: A Quantitative Approach", "John Hennessy")])



# When an error occurs, or exception as we call it,
# Python will normally stop and generate an error message.
try:
    serversocket.bind((host,port))
# except socket.error as e:
# print(str(e))
except:
    print("Sth Went wrong during binding! ")

# _____________________________________________________________

security_array = [("ali","1985"),("amir","1998"),("hamid","2000")]

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
    check = connection.recv(2048)
    check = check.decode("UTF-8")
    check_array = check.split()
    if (check_array[0],check_array[1]) in security_array:
        print("authentication was successful :)")
        student = Student()
        connection.sendall(str.encode("yes"))
        while True:
            # time.sleep(20)
            print("Check222222")
            # print("Array value is: ", r_array[0])
            data = connection.recv(2048)
            print("Check33333")
            # print("recievd method:  ", data.decode("UTF-8"))
            data = data.decode("UTF-8")
            choice = int(data)
            print("Check4444")
            print("choose is :" , choice)



            if choice == 1:
                data = library.displayAvailablebooks()
                connection.sendall(str.encode(data))



            elif choice == 2:
                connection.sendall(str.encode("send info"))
                data = connection.recv(2048)
                data = data.decode("UTF-8")
                data_aray = data.split("@")
                arg1 = data_aray[0]
                arg2 = data_aray[1]
                print("cout: ", arg1, arg2)
                array = student.get_array()
                data = library.lendBook(arg1, arg2, array)
                connection.sendall(str.encode(data))



            elif choice == 3:
                # arg3, arg4 = student.addBook()
                array = student.get_array()
                library.addBook(student)
            elif choice == 4:
                connection.close()
            # with stdoutIO() as s:
            #     exec(data)
            #
            # print("out:", s.getvalue())

            if not data:
                break

            # connection.sendall(str.encode(s.getvalue()))
            # connection.sendall(str.encode(data))

        # connection.close()
    else:
        print("authentication was unsuccessful :(")
        global ThreadCount
        if ThreadCount > 0:
            ThreadCount -= 1
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


    print("Current server status and Threadnumbers is: " + str(ThreadCount))
socketserver.close()