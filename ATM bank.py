# A Small  Bank ATM Application using Class
class Bank:
    def __init__(self):
        self.closingBal = 0

    def display(self):
        print("Enter Your Options:")
        print("1 for deposit:\n2 for withdraw:")
        getoption = input()
        if getoption == "1":
            self.deposit()  # It refers the current instance of class.Whichever instance calls the method.
        elif getoption == "2":
            self.withdraw()
        elif getoption != 1 or getoption != 2:
            print("Thanks")
            return
        print("Your Closing Balance is:",self.closingBal)
        print("Do you want to Continue:")
        a = input()
        if a == "Y" or a == "y":
            self.display()
        else:
            print("Thanks for visiting our Bank")

def deposit(self):
        depositAmount = int(input("Enter your Deposit Amount:"))
        self.closingBal = self.closingBal + depositAmount
        return self.closingBal

def withdraw(self):
        withdrawAmount = int(input("Enter your Withdraw Amount:"))
        if self.closingBal >= withdrawAmount:
            self.closingBal = self.closingBal - withdrawAmount
            print("After withdraw your Balance amount is:", self.closingBal)
        else:
            print("No Sufficient balance")
        return self.closingBal

bankobj =Bank()
bankobj.display()
