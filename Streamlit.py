import streamlit as st
import CBDC
import Account
import Transaction
import Security 
import UserInterface
import matplotlib.pyplot as plt

# Hier importieren Sie Ihre anderen Module und Klassen

# Initialisierung Ihrer CBDC-Simulation

cbdc = CBDC.CBDC("MyCBDC", 1000)
user_interface = UserInterface.UserInterface(cbdc)

# Streamlit-App
def main():
    st.title("CBDC Wallet")

    menu = ["Create Account", "Check Balance", "Transfer CBDC", "Transaction History", "Account Statement"]
    choice = st.sidebar.selectbox("Select an option", menu)

    if choice == "Create Account":
        st.subheader("Create Account")
        user_interface.create_account()

    elif choice == "Check Balance":
        st.subheader("Check Balance")
        account_id = st.text_input("Enter your account ID:")
        if account_id:
            balance = user_interface.check_balance(account_id)
            st.write(f"Account Balance: {balance} CBDC")

    elif choice == "Transfer CBDC":
        st.subheader("Transfer CBDC")
        sender_id = st.text_input("Enter sender account ID:")
        receiver_id = st.text_input("Enter receiver account ID:")
        amount = st.number_input("Enter amount to transfer:", min_value=0)
        if st.button("Transfer"):
            user_interface.transfer_cbdc(sender_id, receiver_id, amount)

    elif choice == "Transaction History":
        st.subheader("Transaction History")
        account_id = st.text_input("Enter account ID:")
        if st.button("Show History"):
            transactions = user_interface.get_transaction_history(account_id)
            for transaction in transactions:
                st.write(f"Amount: {transaction.amount} CBDC, Timestamp: {transaction.timestamp}")

    elif choice == "Account Statement":
        st.subheader("Account Statement")
        account_id = st.text_input("Enter account ID:")
        if st.button("Generate Statement"):
            statement = user_interface.generate_account_statement(account_id)
            st.write(statement)
    elif choice == "Check Balance":
        st.subheader("Check Balance")
        account_id = st.text_input("Enter your account ID:")
        if account_id:
            balance = user_interface.check_balance(account_id)
            st.write(f"Account Balance: {balance} CBDC")
            
            # Grafische Darstellung
            balance_history = user_interface.get_balance_history(account_id)
            plt.plot(balance_history)
            plt.title("Balance History")
            plt.xlabel("Transaction")
            plt.ylabel("Balance")
            st.pyplot(plt)

            # Benutzerprofil
            profile = user_interface.get_user_profile(account_id)
            st.write("User Profile:")
            st.write(f"Name: {profile['first_name']} {profile['last_name']}")
            st.write(f"Birth Date: {profile['birth_date']}")
            st.write(f"Address: {profile['address']}")
    

if __name__ == "__main__":
    main()

