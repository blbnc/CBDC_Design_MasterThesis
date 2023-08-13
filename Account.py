import Transaction
import datetime 

class Account:
    def __init__(self, account_id, balance, public_key):
        self.account_id = account_id
        self.balance = balance
        self.public_key = public_key
        self.transactions = []

    def transfer(self, amount, receiver_account):
        # ... Ihre bisherige Implementierung
        transaction = Transaction.Transaction(self, receiver_account, amount, datetime.now())
        self.transactions.append(transaction)
        receiver_account.transactions.append(transaction)

    def get_balance(self):
        return self.balance

    def transfer(self, amount, receiver_account):
        if self.balance >= amount:
            self.balance -= amount
            receiver_account.receive(amount)

    def receive(self, amount):
        self.balance += amount

    def generate_account_statement(self):
        statement = f"Account Statement for {self.account_id}\n"
        statement += f"Balance: {self.balance} CBDC\n"
        statement += "Transaction History:\n"

        for transaction in self.transactions:
            statement += f"Amount: {transaction.amount} CBDC, Timestamp: {transaction.timestamp}\n"

        return statement

