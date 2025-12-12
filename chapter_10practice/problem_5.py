# write a class train which has methods to book a ticket, get status (no of sets).
# and get fair information of train runnning under the indian railway

from random import randint
class train:
    def __init__(self,trainno):
        self.trainno = trainno
    def book(self,fro,to):
        print(f"ticket is booked in train no {self.trainno} from {fro} to {to}")
        
    def getstatus(self):
        print(f"train no {self.trainno} is running o time")
    

    def getfare(self,fro,to):
        print(f"ticket fare is train no {self.trainno} from {fro} to {to} is {randint(222,5555)}")


t = train(1233)
t.book("jaipur","jodhpur")
t.getstatus()
t.getfare("jaipur",'jodhpur')
