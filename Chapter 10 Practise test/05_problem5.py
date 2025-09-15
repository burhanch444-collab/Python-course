from random import randint
class train:

    def __init__(self, trainNo): 
        self.trainNo = trainNo
    
    def book(self,fro,to):
        print(f"Ticket is booked is train no: {self.trainNo} from {fro} to {to} ")

    def getstatus(self):
        print(f"Train no is: {self.trainNo} is running on time")

    def getfare(self,fro,to):
        print(f"Ticket fare is train no: {self.trainNo} from {fro} to {to} is  {randint(222, 5555)}")
       

t = train(12234)
t.book("sailkot", "lahore")
t.getstatus()
t.getfare("sailkot", "lahore")