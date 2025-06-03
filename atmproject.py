# ATM Simulation Project using functions and return values

def show_menu():
    print("\n===== ATM Main Menu =====")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def check_balance(balance):
    print(f"\nYour current balance is: ₹{balance}")

def deposit_money(balance):
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > 100000:
            print("Maximum deposit limit is ₹100000.")
        else:
            balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Updated balance: ₹{balance}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return balance

def withdraw_money(balance):
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        if amount <= 0:
            print("Amount must be greater than 0.")
        elif amount > 100000:
            print("Maximum withdrawal limit is ₹100000.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Remaining balance: ₹{balance}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return balance

def exit_program():
    print("\nThank you for using the ATM. Have a great day!")

# Main function
def main():
    balance = 10000 
    print("***** Welcome to the ATM Simulator *****")

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit_money(balance)
        elif choice == "3":
            balance = withdraw_money(balance)
        elif choice == "4":
            exit_program()
            break
        else:
            print("Invalid choice. Please select a valid option.")


# Entry point
if __name__ == "__main__":
    main()