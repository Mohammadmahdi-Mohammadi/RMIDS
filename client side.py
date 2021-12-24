# from tkinter import *
# from functools import partial
#
# def validateLogin(username, password):
# 	print("username entered :", username.get())
# 	print("password entered :", password.get())
# 	tkWindow.destroy()
# 	print("verify your account")
# 	return username.get(),password.get()
#
#
# #window
# tkWindow = Tk()
# tkWindow.geometry('200x100')
# tkWindow.title('Login')
#
# #username label and text entry box
# usernameLabel = Label(tkWindow, text="User Name").grid(row=1, column=0)
# username = StringVar()
# usernameEntry = Entry(tkWindow, textvariable=username).grid(row=1, column=1)
#
# #password label and password entry box
# passwordLabel = Label(tkWindow,text="Password").grid(row=2, column=0)
# password = StringVar()
# passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=2, column=1)
#
# validateLogin = partial(validateLogin, username, password)
#
# #login button
# loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=3, column=1)
#
#
#
# tkWindow.mainloop()
# print("salaaaaaaaaaaaaaaaaaaam")



# Task - create a program for a Library, where Students can take out and return books. The library can lend, and update the collection (when a student returns books)
# Here we will be demonstrating abstraction and encapsulation (more on encaspulation later)
# =======For the Library Class, layers of abstraction ==> *display available books, *lend books, *add books
# =======For the Student Class, layers of abstraction: ==> *request a book* and *return a book*
# Note for abstraction: You are only dealing with the important and relevant details of a library...not the irrevelant details like no. of shelves, or the cobwebs on the cielings!

import sys


class Library:
	def __init__(self, listofbooks):  # this init method is the first method to be invoked when you create an object
		# what attributes does a library in general have? - for now, let's abstract and just say it has availablebooks (we're not going to program the shelves, and walls in!)
		self.availablebooks = listofbooks

	def displayAvailablebooks(self):
		print("The books we have in our library are as follows:")
		print("================================")
		for book in self.availablebooks:
			print(book)

	def addBook(self, student_array):
		for book in student_array:
			print(book)
		# self.availablebooks.append((returnedBook,author))
		print("Thanks for returning your borrowed book")

	def lendBook(self, requestedBook, requestedBook_author, student_array):
		if (requestedBook,requestedBook_author) in self.availablebooks:
			print("The book you requested has now been borrowed")
			self.availablebooks.remove((requestedBook,requestedBook_author))
			student_array.append((requestedBook,requestedBook_author))
		else:
			print("Sorry the book you have requested is currently not in the library")



class Student:
	Borrowed_list = [("None", "None")]

	def get_array(self):
		return self.Borrowed_list

	def requestBook(self):
		print("Enter the name of the book you'd like to borrow: ")
		self.book = input()
		print("Enter the name of the author: ")
		self.author = input()
		return self.book,self.author

	def returnBook(self):
		print("Enter the name of the book you'd like to return>>")
		self.book = input()
		return self.book


def main():
	library = Library([("The Soul of a New Machine", "Tracy Kidder"),
					   ("Software and Hardware Problems and Solutions", "Simon Monk"),
					   ("Fundamentals of Superscalar Processors", "John Shen"),
					   ("AStructured Computer Organization", "Andrew Tanenbaum"),
					   ("Computer Networking: A Top Down Approach", "James Kurose"),
					   ("Computer Architecture: A Quantitative Approach", "John Hennessy")])
	student = Student()
	done = False
	while done == False:
		print(""" ======LIBRARY MENU=======
                  1. Display all available books
                  2. Request a book
                  3. Return a book
                  4. Exit
                  """)
		choice = int(input("Enter Choice:"))
		if choice == 1:
			library.displayAvailablebooks()
		elif choice == 2:
			arg1,arg2 = student.requestBook()
			print("cout: ",arg1,arg2)
			array = student.get_array()
			library.lendBook(arg1,arg2,array)
		elif choice == 3:
			# arg3, arg4 = student.addBook()
			library.addBook(student.get_array())
		elif choice == 4:
			sys.exit()


main()
