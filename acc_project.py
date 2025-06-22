# We create first class to defined the things.
# class Name is Account.
#--------------------------------------------
class Account:
    # we create a __init__ (constructor) with def function.
    def __init__(self,bal,acc,name,password): # These "self" is a object reference.
        self.balance = bal
        self.account_no = acc
        self.name = name
        self.password = password
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
#--------------------------------------------
# Get a accountant(user) name.
name = input("Enter the account's holder name:")
#--------------------------------------------
# Get a password by the accountant(user).
while True:
    try:
        password = input("\nEnter your password(minimum 8 characters):")
        if len(password) >= 8:
            break
        else: 
            raise ValueError("Password too short.")
    except ValueError as Ve:
        print("Invalid input:",Ve)
#--------------------------------------------
# Get 12 digit in account number.
while True:
    acc_no = input("\nEnter the 12-digit bank account number:-")
    if acc_no.isdigit() and len(acc_no) == 12:
        acc_no = int(acc_no)
        break
    else: print("Invalid account number.Please enter exactly 12 digits.")
#--------------------------------------------
# Get balance by the accountants.
while True:
    try:
        balance = int(input("\nEnter the bank balance: Rs."))
        break
    except ValueError:
        print("Invalid input.Please enter a numberic value.")
#--------------------------------------------
# Create account Object:
acc1 = Account(balance,acc_no,name,password)
#--------------------------------------------
# password verification give attempt 3 times.
for _ in range(3):  # allow max 3 attempt
    entered_pass = input("\nEnter your password to proceed:")
    if entered_pass == acc1.password:
        break
    else: print("Incorrect password.")
else:
    print("Too many incorrect attempts.Exiting..")
    exit()
#--------------------------------------------