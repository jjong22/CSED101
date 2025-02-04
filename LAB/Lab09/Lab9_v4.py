class BankAccount:
    def __init__(self, name="none", balance=0):
        self.balance = balance
        self.name = name
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance - amount >= 0:
            self.balance -= amount
            return True
        else:
            print("잔액 부족!")
            return False

    def get_info(self):
        print("이름: %s, 잔고: %d" % (self.name, self.balance))
           
    def transfer(self, other, amount):
        if self.withdraw(amount) == True:
            other.deposit(amount)

    def __str__(self):
        return "이름: %s, 잔고: %d" % (self.name, self.balance)

# 테스트 코드
if __name__ == "__main__":
    acc1 = BankAccount("고길동", 1000)
    acc2 = BankAccount("고영희", 200)
    acc1.transfer(acc2, 3000)
    acc1.get_info()
    acc2.get_info()

