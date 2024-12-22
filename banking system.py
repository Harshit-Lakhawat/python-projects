def show_balance(balance):
    print(f"your balance is ${balance:.2f}")

def deposit():
    amount = float(input("enter an amount to be deposited : "))
    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("enter amount to withdraw :"))
    if amount > balance:
        print("insufficient funds")
        return 0
    elif amount < 0:
        print("amount must be greater then 0")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("enter your choice (1-4) : ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            withdrawal_amount = withdraw(balance)
            if withdrawal_amount > 0:
                balance -= withdrawal_amount
        elif choice == '4':
            is_running = False
        else:
            print("That is not a valid choice")

    print("Thank You have a great day ")

main()
