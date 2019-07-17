
class Amit:


    # this is a init/special function
    def __init__(self,fname,lname):

        self.fname = fname
        self.lname = lname


    def full_name(self):

        return self.fname + self.lname


obj1 = Amit("Narendra","Modi") # called init()

obj2 = Amit("Amit","shah")  # called init()

obj1.fname

obj1.lname

obj1.full_name()

obj2.fname

obj2.lname

obj2.full_name()

