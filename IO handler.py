# import socket
# import threading
# import _thread
#
#
# class university:
#     def __init__(self):
#
#         self.country = "Iran"
#         self._city = "Tehran"
#         self._address = "No. 350, Hafez Ave, Valiasr Square"
#         self.name = "Amirkabir University of Technology"
#         self.contact_array =  {"tel" : "+98(21)66419506" , "fax" : "+98(21)66495519" , "email" : "phee@aut.ac.ir"}
#
#     def contact_Info(self):
#         return self.contact_array
#     def phone(self):
#         print(self.address)
#         return self.country
#
# AUT = university()
# data = "AUT.phone()"
# # print(AUT.city)
#
# # -----------------------------------------------------------------------------------
# # https://stackoverflow.com/questions/3906232/python-get-the-print-output-in-an-exec-statement
# # Since Python 3.4 there is a solution is the stdlib:
#
# import sys
# from io import StringIO
# import contextlib
#
# @contextlib.contextmanager
# def stdoutIO(stdout=None):
#     old = sys.stdout
#     if stdout is None:
#         stdout = StringIO()
#     sys.stdout = stdout
#     yield stdout
#     sys.stdout = old
#
#
# with stdoutIO() as s:
#     exec(data)
#
# print("out:", s.getvalue())
#
# # -----------------------------------------------------------------------------------











































































