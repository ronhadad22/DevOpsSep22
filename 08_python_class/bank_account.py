"""
Create a bank account class that has two attributes:

* owner
* balance

and two methods:

* deposit
* withdraw

As an added requirement, withdrawals may not exceed the available balance.
Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.
"""

import python_katas.kata_4.questions as fd


print(f"test {fd.my_singleton2}")
class Account:
    _curency = "$"
    _overdraft = -1000

    @staticmethod
    def currency_value():
        return 3.47

    def __init__(self, owner_arg, balance_arg="dd"):
        self.owner = owner_arg
        self.balance = balance_arg

    def __add__(self, other):
        if not isinstance(other, Account):
            print("Bad operation")
            return

        return Account(self.owner + other.owner, self.balance+ other.balance)

    def __str__(self):
        return f'the account balance is :{self.balance} & the owner is {self.owner}'
    def __iter__(self):

    def __int__(self):
        return 4
    def withdraw(self, amount):
        if not isinstance(amount, int):
            print("withdrawl denied")
        elif self.balance-amount <= Account.overdraft:
            print("cant withdrw this amount")
        else:
            self.balance -= amount
            print (f'withdrwal accepted. current balance: {self.balance}')



class StudentAccount(Account):
    _instance=False
    def __init__(self, name,balance, uni, withdrwal_thershuld = -300):

        super().__init__(name, balance)
        self.uni = uni
        self.withdrwal_thershuld = withdrwal_thershuld

    def withdraw(self, amount):
        if self.balance - amount < self.withdrwal_thershuld:
            print (f'withdrwal limit is {self.withdrwal_thershuld}')
        else:
            super().withdraw(amount)




if __name__ == '__main__':

    shoham = Account("shoham",1000)
    yossi = Account("yossi",100)
    ziv = Account("shoam",100)

    print(shoham.balance)

    # 1. Instantiate the class
    joint_account = shoham + yossi
    print(yossi)
    str(yossi)
    int(yossi)

    yossi.overdraft = -2000
    # 2. Print the object
    print(f"id is: {ziv.owner}")
    print(f"id is: {yossi.owner}")

    print(f"id is: {id(ziv)}")
    print(f"id is: {id(yossi)}")

    # output:
    # >> Account owner:   Jose
    # >> Account balance: $100

    # 3. Show the account owner attribute
    coral = StudentAccount("coral", 95, "bgu")
    coral.withdraw(900)
    print(coral)
    str(coral)
    coral.discount(900)
    michal = StudentAccount("michal",77,"hit")
    # >> 'Jose'

    # 4. Show the account balance attribute

    # >> 100

    # 5. Make a series of deposits and withdrawals

    # >> Deposit Accepted


    # Withdrawal Accepted

    # 6. Make a withdrawal that exceeds the available balance

    # Funds Unavailable!


