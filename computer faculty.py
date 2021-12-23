
class university:
    def __init__(self):

        self.country = "Iran"
        self.city = "Tehran"
        self.address = "No. 350, Hafez Ave, Valiasr Square"
        self.name = "Amirkabir University of Technology"
        self.contact_array =  {"tel" : "+98(21)66419506" , "fax" : "+98(21)66495519" , "email" : "phee@aut.ac.ir"}

    def contact_Info(self):
        return self.contact_array


#
# class  Library(university):
#
#     def __init__(self):







    mycode = 'print ("hello world")'
    exec(mycode)
