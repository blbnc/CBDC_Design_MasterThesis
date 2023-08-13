import streamlit as st
import CBDC
import Account
import Transaction
import Security 
import UserInterface

# Hier importieren Sie Ihre anderen Module und Klassen

# Initialisierung Ihrer CBDC-Simulation
cbdc = CBDC.CBDC("MyCBDC", 1000)
user_interface = UserInterface.UserInterface(cbdc)

# Streamlit-App
def main():
    st.title("CBDC Wallet")

    menu = ["Create Account", "Check Balance", "Transfer CBDC"]
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

if __name__ == "__main__":
    main()
