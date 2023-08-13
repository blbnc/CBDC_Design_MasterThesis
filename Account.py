class Account:
    def __init__(self, account_id, balance, public_key):
        self.account_id = account_id
        self.balance = balance
        self.public_key = public_key

    def get_balance(self):
        return self.balance

    def transfer(self, amount, receiver_account):
        if self.balance >= amount:
            self.balance -= amount
            receiver_account.receive(amount)

    def receive(self, amount):
        self.balance += amount
