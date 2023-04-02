class Account:
    def __init__(p1, Name: str, Surname: str, Balance: int):
        p1.name_surname = Name + "_" +Surname
        p1.balance = Balance
    def deposit(self, money: int):
        self.balance += money 
    def balance_check(self):
        print("Balance:", self.balance, "tg")
    def withdraw(self, How_much: int):
        if self.balance - How_much <= 0:
            print("No money in the deposit")
        else:
            self.balance -= How_much

user1 = Account("Dana", "Sadanova", 5000)
user1.deposit(100000)
user1.balance_check()
user1.withdraw(20000)
user1.balance_check()
user1.withdraw(100000)

