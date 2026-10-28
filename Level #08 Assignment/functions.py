import random

class BankAccount:
    #initializing constants
    def __init__ (self, name):
        
        self.number = random.randint(100000, 999999)
        self.balance = 0.0
        self.name = name

    # Creating methods for each instance
    def deposit(self):
        deposit = 0
        try:
            deposit = float(input("\nHow much would you like to deposit? \n"))
        except ValueError:
            print("Invalid input, try again.")
        if deposit <= 0:
                print("Please enter a number greater than zero.")
        self.balance += deposit
        return

    def withdrawl(self):
        while True:
            try:
                amount = float(input("\nHow much would you like to withdraw? \n"))
            except ValueError:
                print("Invalid input, try again.")

            if self.balance < amount:
                print("You can't withdraw more than you have.")
            elif self.balance <= 0:
                print("Please enter a number greater than zero.")
            else:
                self.balance -= amount
            return self.balance
    
    def view_account_info(self):
        print(f"Account name: {self.name}")
        print(f"Account number: {self.number}")
        print(f"Balance: ${self.balance:.2f}")
    
    # Keep each option a method called within the class
    def choose_option (self):
        while True:
            print("\nPlease choose an option: \n")
            try:
                user_input = int(input(("1. Make a deposit\n2. Make a withdrawl\n3. View account information\n4. Quit\n\n")))
            except ValueError:
                print("Invalid choice, please try again.")
                continue
            if user_input == 1:
                self.deposit()
            elif user_input == 2:
                self.withdrawl()
            elif user_input == 3:
                self.view_account_info()
            elif user_input == 4:
                print("Thank you for doing business with a pretty awesome bank.")
                return
            else:
                print("Invalid choice, please try again.")





    
    

    
    

    


