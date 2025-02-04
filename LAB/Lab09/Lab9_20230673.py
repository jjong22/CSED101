class BankAccount:
    def __init__(self, name="none", balance=0):
        self.balance = balance
        self.name = name
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
        else:
            print("잔액 부족!")

    def get_info(self):
        print("이름: %s, 잔고: %d" % (self.name, self.balance))
           
    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)

class MinimumBankAccount(BankAccount):
    def __init__(self, name="none", balance=0, min_bal=0):
        super().__init__(name, balance)
        self.min_bal = min_bal

    def withdraw(self, amount):
        if self.balance - amount >= self.min_bal:
            self.balance -= amount
        else:
            print("최소 잔액을 유지해야 합니다")