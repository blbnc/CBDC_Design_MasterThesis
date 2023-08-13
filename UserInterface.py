#coding=utf-8
import Security

class UserInterface:
    def __init__(self, cbdc):
        self.cbdc = cbdc

    def create_account(self):
        # Benutzereingaben für Kontoerstellung abfragen
        # Generiere Schlüsselpaar
        private_key, public_key = Security.generate_key_pair()
        account_id = input("Enter account ID: ")
        initial_balance = float(input("Enter initial balance: "))
        self.cbdc.create_account(account_id, initial_balance, public_key)

    # Weitere Methoden für Benutzereingaben und -interaktionen
