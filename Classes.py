class user:

  def __init__(self):
    self.wallet = 0
    self.bank = 0
    self.total = bank + wallet
    self.inventory = {}  #item:count
    self.safetyamount = 50
    print(f"Initialising user {str(self)}")

  def safetyamount(self, amount: int):
    self.safetyamount = amount

  def getmoney(self, loc: str):
    if loc == 'wallet':
      return self.wallet
    elif loc == 'bank':
      return self.bank
    elif loc == 'total':
      return self.total

  def addmoney(self, amount: float):
    if amount <= 0:
      print('cant add negative/zero money')

    else:
      self.bank += amount
      print(f"{amount} has been added, bank balance is now {self.bank}")

  def takemoney(self, amount):
    if amount >= self.bank - self.safetyamount:
      print(f"Cant take more money than {self.bank - self.safety}")
    else:
      return amount
      self.bank -= amount