class Account:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, new_mon):
        self.balance += new_mon
        
    def withdraw(self, Withdrawal):
        if self.balance >= Withdrawal:
            self.balance -= Withdrawal
            return self.balance
        else:
            return "Insufficient Funds"
        
balance, withdrawal = map(int, input().split())

p1 = Account(balance)
print(p1.withdraw(withdrawal))
    
