class Category:
  def __init__(self,name):
    self.name = name
    self.ledger = []
    

  def deposit(self,amount,description=""):
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self,amount,description=""):
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False
  
  def get_balance(self):
    return sum(item["amount"] for item in self.ledger)

  def transfer(self,amount,category):
    if self.check_funds(amount):
      self.withdraw(amount,f"Transfer to {category.name}")
      category.deposit(amount,f"Transfer from {self.name}")
      return True
    return False

  def check_funds(self,amount):
    return self.get_balance()>=amount
    
  def __str__(self):
    title=self.name.center(30,"*")
    items=""
    for item in self.ledger:
      description = item["description"][:23]
      amount = "{:.2f}".format(item["amount"])
      items += f"{description:<23}{amount:>7}\n"
    total = "Total: {:.2f}".format(self.get_balance())
    return f"{title}\n{items}{total}"
      

def create_spend_chart(categories):
  category_name = []
  spent = []
  for category in categories:
    total_spent = 0
    for item in category.ledger:
      if item["amount"] < 0:
        total_spent -= item["amount"]
    spent.append(round(total_spent,2))
    category_name.append(category.name)
  total_spent = round(sum(spent),2)
  percentages = [i/total_spent*100 for i in spent]

  chart = "Percentage spent by category\n"
  for i in range(100,-10,-10):
    chart += f"{i:>3}| "
    for percent in percentages:
      if percent >= i:
        chart += "o  "
      else:
        chart += "   "
    chart += "\n"
  chart += "    " + "-" * (len(categories) * 3 + 1)
  max_len = max(len(name) for name in category_name)
  for i in range(max_len):
    chart += "\n     "
    for name in category_name:
      if len(name) > i:
        chart += name[i] + "  "
      else:
        chart += "   "
  return chart