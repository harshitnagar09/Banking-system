class BankAccount:

  def __init__(self,balance,account_no,account_holder_name):
    self.balance = balance
    self.account_no = account_no
    self.account_holder_name = account_holder_name
  
  def display(self):
    print("Here are your account details:")
    print("Account Holder :",self.account_holder_name)
    print("Account Number : ",self.account_no)
    print("Balance : ",self.balance)
  
  def credit(self,credit_amount):
    self.balance = self.balance + credit_amount
    print(credit_amount ,"credited to your account\nYour Balance :",self.balance)
  
  def debit(self,amount):
    if amount>self.balance:
      print("Insufficient balance",self.balance)
    else:
      self.balance-= amount
      print(amount,"Debit from your account")
      print("Remaining balance : ",self.balance)

accounts = []
no_of_accounts = 100000

while True:
    print(
  "Press 1 if you want open account\n"
  "Press 2 if you want to Deposit money\n"
  "Press 3 if you want to withdraw money\n"
  "Press 4 if you want to check balance\n"
  "Press 5 For Exit"
)   
    try:
      a = int(input("Enter Your choice: "))
    except ValueError:
      print("Please enter a valid number.")
      continue
   
    if 1==a:
      name = input("Enter your Name: ").strip()
      if not name:
        print("Name cannot be empty.")
        continue              # go back to menu
  
      try:
        initial_deposit = int(input("Enter the amount of initial deposit: "))
        if initial_deposit <= 0:
          print("Amount must be greater than 0.")
          continue

      except ValueError:
        print("Please enter a valid number.")
        continue
      acc = BankAccount(initial_deposit,no_of_accounts,name)
      accounts.append(acc)
      print("Your Account is created")
      acc.display()
      no_of_accounts +=1


    elif 2==a:
      
      try:
        account_number = int(input("Enter your Account Number: "))
      except ValueError:
        print("Please enter a valid number.")
        continue

      found = False
      for i in accounts:
        if i.account_no==account_number:
          found = True
          try:
            deposit = int(input("Enter the deposit amount: "))
            if deposit <= 0:
              print("Amount must be greater than 0.")
              break

          except ValueError:
            print("Please enter a valid number.")
            break

          i.credit(deposit)
          i.display()
          break
      if not found:
        print("You do not have an account in our bank or Enter a valid account number ")
          
      
    elif 3==a:
      
      try:
        account_number = int(input("Enter your Account Number: "))
      except ValueError:
        print("Please enter a valid number.")
        continue

      found = False
      for i in accounts:
        if i.account_no==account_number:
          found = True
          try:
            withdraw = int(input("Enter the Amount you want Withdraw: "))
            if withdraw <= 0:
              print("Amount must be greater than 0.")
              break
          except ValueError:
            print("Please enter a valid number.")
            break
          i.debit(withdraw)
          i.display()
          break
      if not found:
        print("You do not have an account in our bank or Enter a valid account number ")
    
    elif 4==a:
      
      try:
        account_number = int(input("Enter your Account Number: "))
      except ValueError:
        print("Please enter a valid number.")
        continue

      found = False
      for i in accounts:
        if i.account_no==account_number:
          found = True
          i.display()
          break
      if not found:
        print("You do not have an account in our bank or Enter a valid account number ")
    elif 5==a:
      break
    else:
      print("Select a Valid Option")
      
    