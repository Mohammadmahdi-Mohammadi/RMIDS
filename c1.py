import socket
from tkinter import *
from functools import partial
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

__user = ""
__pass = ""
def validateLogin(username, password):
    global __user,__pass
    print("username entered :", username.get())
    print("password entered :", password.get(),"\n","we are going to verify your account ... ")
    # print("we are going to verify your account")

    __user = username.get()
    # print("salaaaam  " , __user)
    __pass = password.get()
    tkWindow.destroy()
    return


#


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

print("current is:    " , __user , __pass)


check = __user + " " + __pass
clientsocket.send(str.encode(check))
response = clientsocket.recv(1024)
response = response.decode("utf-8")
if response == "yes":
    print("authentication was successful :)")
    print(""" ======LIBRARY MENU=======
                      1. Display all available books
                      2. Request a book
                      3. Return a book
                      4. Exit
                      """)

    while True:
        print("Check1111111")

        Input = input("Enter Choice:")
        # print("Check222222")
        # print(type(Input))
        while ( not Input.isnumeric()):
            Input = input("Please enter a number! : ")

        print("input is: ", Input)
        if int(Input) == 1:
            print("Check33333")

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
        print("     =================================================== ")
        if int(Input) == 2:
            clientsocket.send(str.encode(Input))
            response = clientsocket.recv(1024)
            response = response.decode("UTF-8")
            print("Enter the name of the book you'd like to borrow: ")
            book = input()
            print("Enter the name of the author: ")
            author = input()
            requestbook = book + "@" + author
            clientsocket.send(str.encode(requestbook))
            response = clientsocket.recv(1024)
            response = response.decode("UTF-8")
            print(response)
            print("Check222222")




        if int(Input) == 3:
            clientsocket.send(str.encode(Input))
            response = clientsocket.recv(1024)
            response = response.decode("UTF-8")
            if "@" in response:
                responses = response.split('@')
                index = 1
                print(responses)
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
                    print("Enter the desired book number in range of 1 to ", index - 1, " : ")
                    booknum = input()
                add_index = int(booknum) - 1
                add_index_final = str(add_index)
                clientsocket.send(str.encode(add_index_final))
                response = clientsocket.recv(1024)
                response = response.decode("UTF-8")
                print(response)



            else:
                print(response)



        # if int(Input) == 4:

        # clientsocket.send(str.encode(Input))
        # response = clientsocket.recv(1024)

else:
    print("authentication was unsuccessful :(")


