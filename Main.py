def main():
    cbdc = CBDC("MyCBDC", 1000)
    user_interface = UserInterface(cbdc)

    while True:
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Transfer CBDC")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_interface.create_account()
        elif choice == "2":
            # Benutzereingaben abfragen und Guthaben abrufen
        elif choice == "3":
            # Benutzereingaben abfragen und CBDC übertragen
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
