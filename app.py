# from calc import deposit_calc, withdraw_calc

import calc as ca

user_data = {
    "username"  : "admin",
    "Acc no"    : 123456789,
    "pin"       : 1234,
    "total bal" : 10000
}

def user_info():
    if user_data and user_data["username"]:
        return f"Hi Welcome user {user_data['username']} Your acc.no is {user_data['Acc no']}"
    else:
        return False

def withdraw(withdraw_amount):
    if withdraw_amount > user_data["total bal"]:
        return False
    else:
        amount = ca.withdraw_calc(user_data["total bal"], withdraw_amount)
        user_data["total bal"] = amount
        return amount

def deposit(deposit_amount):
    if deposit_amount:
        amount = ca.deposit_calc(user_data["total bal"], deposit_amount)
        user_data["total bal"] = amount
        return amount
    else:
        return False

def check_balance():
    return user_data["total bal"]

def main():
    print("Welcome to TP ATM")
    print("="*20)

    pin = int(input("Enter your pin no to proceed: "))

    if pin == user_data['pin']:
        print(user_info())

        while True:
            choice = int(input("1. Withdraw\n2. Deposit\n3. Check Balance\n4. Exit\nEnter your choice: "))

            match choice:
                case 1:
                    amount = int(input("Enter amount to withdraw: "))
                    withdraw_resp = withdraw(amount)
                    if withdraw_resp:
                        print(f"Withdraw successful. Your total balance is {withdraw_resp}")
                    else:
                        print("Insufficient balance")

                case 2:
                    amount = int(input("Enter amount to deposit: "))
                    print(f"Deposit successful. Your total balance is {deposit(amount)}")

                case 3:
                    print(f"Your total balance is {check_balance()}")

                case 4:
                    print("Thank you for using TP ATM.")
                    break

                case _:
                    print("Invalid choice. Please choose between 1 to 4")

    else:
        print("Invalid pin. Please try again")
        return

if __name__ == "__main__":
    main()