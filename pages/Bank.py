class Bank_Account:

    def __init__(self,owner,balance):

        self.owner = owner
        self.balance = balance

    def deposit(self,deposit):

        self.balance += deposit
        print ('Deposit accepted')

    def withdraw(self,withdraw):

        if self.balance > withdraw:
            self.balance -= withdraw
            print('Withdrawal Accepted')
        else:
            print('Funds Unavailable!')


owner = 'Jose'
balance = 100

ba = Bank_Account(owner,balance)

print ('Owner name is ' +ba.owner)
print ('{} has balance of {}'.format(ba.owner,ba.balance))
ba.deposit(100)
print ('After deposit {} has balance of {}'.format(ba.owner, ba.balance))
ba.withdraw(200)
print ('After deposit {} has balance of {}'.format(ba.owner, ba.balance))