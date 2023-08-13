class Transaction:
    def __init__(self, sender, receiver, amount, timestamp):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = timestamp

    def get_transaction_history(self, account_id):
        if account_id in self.accounts:
            account = self.accounts[account_id]
            return account.transactions
        else:
            print("Account not found.")
            return []
