import socket
from tkinter import *
from functools import partial

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
print(Response.decode("utf-8"))



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

    while True:
        Input = input("say something")
        clientsocket.send(str.encode(Input))
        response = clientsocket.recv(1024)
        print((response.decode("utf-8")))
else:
    print("authentication was unsuccessful :(")


