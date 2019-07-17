

class grandfather:

    def fun(self):

        print("I am granfather function")

    def funxx(self):

        print("I am granfatherx function")


class father:

    def fun1(self):

        print("I am father function")


    def funxx(self):

        print("I am fatherx function")

class son(grandfather,father):

    def fun3(self):

        print("I am son function")


sn =son()

sn.funxx()

'''sn.fun3()

sn.fun()

sn.fun1()

fn =father()

fn.fun1()'''



