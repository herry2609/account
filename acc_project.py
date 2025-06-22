# We create first class to defined the things.
# class Name is Account.
class Account:
    # we create a __init__ (constructor) with def function.
    def __init__(self,bal,acc,name,pwd): # These "self" is a object reference.
        self.balance = bal
        self.account_no = acc
        self.name = name
        self.password = pwd
    # We create name of the user or accountants.
    def get_name(self): 
        return self.name
    # We create password for the accountants(user).
    def get_pass(self):
        return self.password
    # We create debit method first.
    def debit(self,amount):
        if amount > self.balance:
            print("Insufficient Balance.")
        else: 
            self.balance -= amount
            print("Rs.",amount,"was debited.")
            print("Total balance :",self.final_bal())
    # We create credit method.
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited.")
        print("Total balance :",self.final_bal())
    # We create a final balance.
    def final_bal(self):
        return self.balance