def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount of money you want to deposit: "))
    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter your amount of money to withdraw: "))
    if amount > balance:
        print("Insuficient funds!")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0!")
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking program")
        print("1. Show balance")
        print("2. Deposit money")
        print("3. Withdraw money")
        print("4. Exit program")

        choice = input("Enter your option (1-->4): ")
        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("That is not a valid choice!")

print("Thank you and have a nice day!")
if __name__=='__main__':
    main()