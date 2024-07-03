import time

print("please insert your card ")

time.sleep(5)
password=1234
pin=int(input("enter your atm pin"))
balance =5000
if pin==password:
    transaction_history = []
print("""1==balance
          2==withdraw balance
          3==deposit balance
          4==change pin
          5==transaction history
          6==exit
          """)
while True:
    try:
        option=int(input("please enter your chice"))
    except:
        print("please enter a valid option")
    if option==1:
        print(f"your balance is{balance}")

    print("==============================================")
    if option==2:
        withdraw_amount=int(input("please enter the amount you want to withdraw"))
        balance=balance-withdraw_amount
        transaction_history.append(f"Withdrawal: ${withdraw_amount}")
        print(f"{withdraw_amount} is debited from your account")
        print(f"your updated balance is {balance}")
        print("==============================================")

    if option==3:
        deposit_amount=int(input("please enter the deposit_amount"))
        balance=balance+deposit_amount
        transaction_history.append(f"Deposit: ${deposit_amount}")
        print(f"{deposit_amount} is credited to your account")
        print(f"your updated balance is {balance}")
        print("==============================================")

    if option==4:
        new_pin = int(input("Enter new PIN: "))
        password = new_pin
        print("PIN successfully changed.")

        print("==============================================")
    if option==5:
            print("\nTransaction History:")
            for transaction in transaction_history:
                print(transaction)
    if option==6:
        break

    else:
        print("please enter a valid option")
    