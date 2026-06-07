import json
import os

class BankAccount:

  def __init__(self,balance,account_no,account_holder_name,account_pin):
    self.balance = balance
    self.account_no = account_no
    self.account_holder_name = account_holder_name
    self.account_pin = account_pin

  
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

class Bankdata:
  
  @staticmethod
  def save_data(accounts , no_of_accounts):
    data = {
      "accounts":[],
      "no_of_accounts":no_of_accounts
    }
    for acc in accounts:
      data["accounts"].append(vars(acc)) 
    with open("accounts.json","w") as file:
      json.dump(data,file,indent=4)
    
  @staticmethod
  def load_data():
    if not os.path.exists("accounts.json"):
      return [], 100000

    with open("accounts.json", "r") as file:
        data = json.load(file)

    accounts = []

    for acc_data in data["accounts"]:
      acc = BankAccount(
          acc_data["balance"],
          acc_data["account_no"],
          acc_data["account_holder_name"],
          acc_data["account_pin"]
    )
      accounts.append(acc)

    return accounts, data["no_of_accounts"]


accounts, no_of_accounts = Bankdata.load_data()

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
        continue             
  
      try:
        initial_deposit = int(input("Enter the amount of initial deposit: "))
        account_pin = int(input("Enter the PIN number: "))
        if initial_deposit <= 0:
          print("Amount must be greater than 0.")
          continue
      except ValueError:
        print("Please enter a valid number.")
        continue

      acc = BankAccount(initial_deposit,no_of_accounts,name,account_pin)
      accounts.append(acc)
      print("Your Account is created")
      acc.display()
      no_of_accounts +=1


    elif 2==a:
      
      try:
        print("Login")
        account_number = int(input("Enter your Account Number: "))
        account_pin = int(input("Enter the pin: "))
      except ValueError:
        print("Please enter a valid number.")
        continue

      found = False
      for i in accounts:
        if i.account_no==account_number:
          found = True
          if i.account_pin != account_pin:   
            print("Incorrect PIN.")
            break
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
        print("Login")
        account_number = int(input("Enter your Account Number: "))
        account_pin = int(input("Enter the pin: "))
      except ValueError:
        print("Please enter a valid number.")
        continue

      found = False
      for i in accounts:
        if i.account_no==account_number:
          found = True
          if i.account_pin != account_pin:   # ← add this
            print("Incorrect PIN.")
            break
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
        print("Login")
        account_number = int(input("Enter your Account Number: "))
        account_pin = int(input("Enter the pin: "))
      except ValueError:
        print("Please enter a valid number.")
        continue

      found = False
      for i in accounts:
        if i.account_no==account_number:
          found = True
          if i.account_pin != account_pin:   # ← add this
            print("Incorrect PIN.")
            break
          i.display()
          break
      if not found:
        print("You do not have an account in our bank or Enter a valid account number ")
    elif 5==a:
      Bankdata.save_data(accounts,no_of_accounts)
      print("Data saved successfully.")
      break
    else:
      print("Select a Valid Option")
  
    