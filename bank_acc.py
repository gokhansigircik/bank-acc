class BankAccount:
    # don't forget to add some default values for these parameters!
  def __init__(self, int_rate=0.1, balance=0): 
    self.int_rate = int_rate
    self.balance = balance


  def deposit(self, amount):
    self.balance += amount
    print(self.balance)
    return self

  def withdraw(self, amount):
    if amount < self.balance:
      self.balance = self.balance - amount
      return self
    else:
      print("Insufficient funds Charging a $5 fee")
      self.balance -= 5
      print(f"your new balance is: ${self.balance}")
      return self


  def display_account_info(self):
    print(self.balance)
    return self

  def yield_interest(self):
      self.balance *= (1 + self.int_rate)
      print(self.balance)
      return self



bank_acc1 = BankAccount(0.1, 100)
bank_acc2 = BankAccount(0.01, 300)

bank_acc1.deposit(10).deposit(20).deposit(40).withdraw(50).yield_interest().display_account_info()
bank_acc2.deposit(20).deposit(30).withdraw(5).withdraw(10).withdraw(15).withdraw(30).yield_interest().display_account_info()

