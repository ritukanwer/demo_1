class amount:
    def __init__(self,balanace,acc):
        self.balanace = balanace
        self.acc = acc
    def debit(self,amount):
        self.balanace -= amount
        print("rs",amount,"was debited")
        print("total balance = ",self.get_balance())
    
    def credit(self,amount):
        self.balanace += amount
        print("rs",amount,"was credited")
        print("total balance = ",self.get_balance())
    
    


    def get_balance(self):
        return self.balanace
    
account1 = amount(10000,9000)
account1.debit(20000)
account1.credit(10000)

# print(account1.balanace)
# print(account1.acc)