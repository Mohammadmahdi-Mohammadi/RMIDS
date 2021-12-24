
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

	def addBook(self, student):
		student_array = student.get_array()
		if len(student_array) > 1:
			print("List of books you have borrowed: ")
			index = 1
			for book in student_array:
				print(index,"- ",book)
				index += 1
			print("Enter the desired book number in range of 1 to ",index - 1," : ")
			booknum = input()
			while (int(booknum) > index or int(booknum) < 1):
				print("Enter the desired book number in range of 1 to ", index - 1, " : ")
				booknum = input()
			add_index = int(booknum) - 1
			self.availablebooks.append((student_array[add_index]))
			student.del_b_book(int(booknum) - 1)
			print("Thanks for returning your borrowed book")

	def lendBook(self, requestedBook, requestedBook_author, student_array):
		if (requestedBook,requestedBook_author) in self.availablebooks:
			print("The book you requested has now been borrowed")
			self.availablebooks.remove((requestedBook,requestedBook_author))
			student_array.append((requestedBook,requestedBook_author))
		else:
			print("Sorry the book you have requested is currently not in the library")



class Student:
	Borrowed_list = []

	def get_array(self):
		return self.Borrowed_list
	def del_b_book(self,index):
		del self.Borrowed_list[index]

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
			array = student.get_array()
			library.addBook(student)
		elif choice == 4:
			sys.exit()


main()
