# --------------------------------------------------------------
# Created by Mohammadmahdi_Mohammadi on 25/12/21.
# available on github.com/Mohammadmahdi-Mohammadi/RMIDS
# --------------------------------------------------------------

#Remote invocation makes the objects and methods of the remote server call
# in much the same way as the local objects and methods, because we hide them
# all by network programming. Remote invocation is the foundation of distributed systems.
# Remote invocation is generally divided into two types, remote procedure call (RPC) and remote method call (RMI)

# RMI
# RMI, which stands for remote method call, is more granular than RPC because its basic unit is an object.
# The general idea is to create an RMI server object, register one of the instantiated objects in the RMI server
# object with the specified service name (it can also be multiple objects, but the service name should not be the same),
# and then start the RMI server. The server waits for the data sent by the client (including the service name, function name, parameters)
# and returns the processing results to the client

# RPC
# RPC belongs to the remote call at the function level, and it mostly transmits data through HTTP
# in the form of XML, JSON, serialized data, etc. Here's an example of xml-rpc in python.
# Ref: ofstack.com/

# -------------------------------------------------------------------------------------------
# function for login interface
# copyright:https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters
# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

# --------------------------------------------------------------

# copyright: https://stackoverflow.com/questions/3906232/python-get-the-print-output-in-an-exec-statement
# Since Python 3.4 there is a solution is the stdlib:

# --------------------------------------------------------------

# uses in code migrations
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
import time
from tkinter import *
from functools import partial

# -------------------------------------------------------------------------------------------

# copyright:https://stackoverflow.com/questions/3173320/text-progress-bar-in-terminal-with-block-characters
# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

# -------------------------------------------------------------------------------------------------------

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

# ------------------------------------------------------------------------------

__user = ""
__pass = ""
def validateLogin(username, password):
    global __user,__pass
    # print("username entered :", username.get())
    # print("password entered :", password.get(),"\n","we are going to verify your account ... ")
    prYellow(   "we are going to verify your account ... ")
    # A List of Items
    items = list(range(0, 300))
    l = len(items)

    # Initial call to print 0% progress
    printProgressBar(0, l, prefix='Progress:', suffix='Complete', length=30)
    for i, item in enumerate(items):
        # Do stuff...
        time.sleep(0.001999)
        # Update Progress Bar
        printProgressBar(i + 1, l, prefix='Progress:', suffix='Complete', length=30)
    # time.sleep(1)
    # prRed("...")
    # time.sleep(1)
    # prRed("...")
    # time.sleep(1)
    # prRed("...")
    # time.sleep(1)
    # print("we are going to verify your account")

    __user = username.get()
    # print("salaaaam  " , __user)
    __pass = password.get()
    tkWindow.destroy()
    return

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 10000

# print("waiting for connections")
try:
    clientsocket.connect((host,port))
except:
    print("Sth Went wrong during binding! ")
# except socket.error as e:
#     print(str(e))

Response = clientsocket.recv(1024)
prGreen(Response.decode("utf-8"))

# --------------------------------------------------------------
# The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit.
# Both Tk and tkinter are available on most Unix platforms, including macOS, as well as on Windows systems.

#window
tkWindow = Tk()
tkWindow.geometry('200x100')
tkWindow.title('Login')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=1, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=1, column=1)

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=2, column=0)
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=2, column=1)

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=3, column=1)

tkWindow.mainloop()

# --------------------------------------------------------------

check = __user + " " + __pass
clientsocket.send(str.encode(check))
response = clientsocket.recv(1024)
response = response.decode("utf-8")
if response == "yes":
    prGreen("         Authentication was successful :)")
    print("you're currently login as -----> ", __user)
    prYellow("""                       ======LIBRARY MENU=======
                      1. Display all available books
                      2. Request a book
                      3. Return a book
                      4. Exit""")

    while True:
        # print("Check1111111")

        Input = input("Enter Choice:")
        # print("Check222222")
        # print(type(Input))
        while ( not Input.isnumeric()):
            Input = input("Please enter a number! : ")

        # print("input is: ", Input)
        if int(Input) == 1:
            # print("Check33333")
            # print("??????????????????")
            clientsocket.send(str.encode(Input))
            response = clientsocket.recv(1024)
            response = response.decode("UTF-8")
            responses = response.split('@')
            i = 1
            for item in responses:
                if i > 2:
                    print("     ",i - 2,"- ",item)
                else:
                    print("     ",item)
                i += 1
        prYellow("     =================================================== ")
        if int(Input) == 2:
            clientsocket.send(str.encode(Input))
            response = clientsocket.recv(1024)
            response = response.decode("UTF-8")
            prGreen("Enter the name of the book you'd like to borrow: ")
            book = input()
            prGreen("Enter the name of the author: ")
            author = input()
            requestbook = book + "@" + author
            clientsocket.send(str.encode(requestbook))
            response = clientsocket.recv(1024)
            response = response.decode("UTF-8")
            prRed(response)
            prYellow("     =================================================== ")

            # print("Check222222")

        if int(Input) == 3:
            clientsocket.send(str.encode(Input))
            response = clientsocket.recv(1024)
            response = response.decode("UTF-8")
            if "@" in response:
                responses = response.split('@')
                index = 1
                # print(responses)
                for book in responses:
                    if index == 1 or index == 2:
                        print("     ", book)
                        index += 1

                    else:
                        print("     ", index - 2, "- ", book)
                        index += 1
                print("Enter the desired book number in range of 1 to ", index - 3, " : ")
                booknum = input()
                while (int(booknum) > index - 1 or int(booknum) < 0):
                    print("\n           Enter the desired book number in range of 1 to ", index - 1, " : ")
                    booknum = input()
                add_index = int(booknum) - 1
                add_index_final = str(add_index)
                clientsocket.send(str.encode(add_index_final))
                response = clientsocket.recv(1024)
                response = response.decode("UTF-8")
                prRed(response)
                prYellow("     =================================================== ")

            else:
                prRed(response)


        if int(Input) == 4:
            print("Connection terminated. ")
            clientsocket.close()
            break

        # clientsocket.send(str.encode(Input))
        # response = clientsocket.recv(1024)

else:
    prRed("         Authentication was unsuccessful :(")
