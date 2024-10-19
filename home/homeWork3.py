

class Bank():
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
    
    def moneyX(self):
        input_amount = float(input('Enter input amount: '))
        self._balance += input_amount
        return f'Current balance: {self._balance}'

    def _kill(self):
        self._balance = 0
        return f'Balance: 0'
    
    def __jackpot(self):
        self._balance *= 10
        return f'Congrats! Your balance: {self._balance}'
    
    def _wtf(self, other):
        self._balance += other._balance
        return f"Баланс объединен. Текущий баланс: {self._balance}"
    
client1 = Bank("Alice", 1000)
client2 = Bank("Bob", 500)

print(client1._kill())
print(client1.moneyX())
print(client1._wtf(client2))
print(client1._Bank__jackpot())
