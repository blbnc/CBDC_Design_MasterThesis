import Account
import UserInterface
import Transaction
import Security


class CBDC:
    def __init__(self, name, total_supply):
        self.name = name
        self.total_supply = total_supply
        self.accounts = {}

    def create_account(self, account_id, initial_balance, public_key):
        if account_id not in self.accounts:
            account = Account(account_id, initial_balance, public_key)
            self.accounts[account_id] = account
            return account
        else:
            print("Account already exists.")

    def get_total_supply(self):
        return self.total_supply

    def issue_cbdc(self, amount):
        self.total_supply += amount

    def transfer_cbdc(self, sender_account, receiver_account, amount):
        sender_account.transfer(amount, receiver_account)
