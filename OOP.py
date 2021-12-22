# # Creates class Car
# class Car:
#
#     # create class attributes
#     car_count = 0
#
#     def __init__(self):
#         print ("Engine started")
#         self.name = "corolla"
#         self.__make = "toyota"
#         self._model = 1999
#
#     # create class methods
#     def start(self, name, make, model):
#         print ("Engine started")
#         self.name = name
#         self.make = make
#         self.model = model
#         Car.car_count += 1
#
#     @staticmethod
#     def get_class_details():
#         print ("This is a car class")
#
#
#
# # In Python, every object has some default attributes and methods in addition
# # to user-defined attributes. To see all the attributes and methods of an object,
# # the built-in dir() function can be used.
# car_b = Car()
# print(dir(car_b))












# Inheritance && Overriding


# Create Class Vehicle
class Vehicle:
    def print_details(self):
        print("This is parent Vehicle class method")

# Create Class Car that inherits Vehicle
class Car(Vehicle):
    def print_details(self):
        print("This is child Car class method")

# Create Class Cycle that inherits Vehicle
class Cycle(Vehicle):
    def print1_details(self):
        print("This is child Cycle class method")



car_a = Vehicle()
car_a. print_details()

car_b = Car()
car_b.print_details()

car_c = Cycle()
car_c.print_details()