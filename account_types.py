from main import BankAccount

class SavingsAccount(BankAccount):
    
    def __init__(self, balance, account_no, account_holder_name,
                 transactions=None, interest_rate=5.0, account_type="savings"):
        # Pass everything up to BankAccount
        super().__init__(balance, account_no, account_holder_name,
                         transactions, account_type)
        self.interest_rate = interest_rate
 
    def apply_interest(self):
        """Increase balance by interest_rate %."""
        interest = round(self.balance * (self.interest_rate / 100), 2)
        self.credit(interest)               # credit() also logs the transaction
        print(f"  Interest {self.interest_rate}% applied → added {interest}")
 
    def display(self):
        super().display()
        print(f"  Interest Rate: {self.interest_rate}%")
        print("-----------------------")


