class Customer:
    bankname='HDFC'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print('After deposit balance is',self.balance)
    def withdraw(self,amount):
        if self.balance<amount:
            print('Insufficient funds...')
        else:
            self.balance=self.balance-amount
            print('After withdrawal balance is',self.balance)
print('Welcome to bank',Customer.bankname)
name=input('Enter your name ')
c=Customer(name)
while True:
    print('d-Deposit\nw-Withdraw\ne-Exit')
    option=input('Choose your option')
    if option.lower()=='d':
        amount=float(input('Enter amt to deposit '))
        c.deposit(amount)
    elif option.lower()=='w':
        amount=float(input('Enter amt to withdraw '))
        c.withdraw(amount)
    elif option.lower()=='e':
        print('Thank you for banking with HDFC')
        break
    else:
        print('Invalid option')
