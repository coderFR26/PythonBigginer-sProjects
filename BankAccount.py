

def show_balance():
    global balance
    return balance

def deposite(amount):
    if amount <= 0:
        print('You cannot deposite zero or less')
        return 0
    global balance
    balance = show_balance() + amount
    return balance


def withdraw(amount):
    global balance
    if amount > balance:
        print('You cannot withdraw more than balance')
        return 0
    balance = show_balance() - amount
    return balance


balance = 100
print('Welcome to Bank Account App')
while True:
    print('What operation would you like to do?')
    print('1. Show Balance')
    print('2. Deposit')
    print('3. Withdraw')
    print('4. Exit')
    operation = int(input('>> '))
    if operation == 1:
        balance = show_balance()
        print(f'Your Balance is: ${balance}')
        continue
    elif operation == 2:
        amount = input('Enter amount to deposit: ')
        if not amount.isdigit():
            print('Please enter a valid amount')
            continue
        amount = int(amount)
        deposite(amount)
        balance = show_balance()
        continue
    elif operation == 3:
        amount = input('Enter amount to withdraw: ')
        if not amount.isdigit():
            print('Please enter a valid amount')
            continue
        amount = int(amount)
        withdraw(amount)
        balance = show_balance()
        continue
    else:
        break



