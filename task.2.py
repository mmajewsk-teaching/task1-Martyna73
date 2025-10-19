#Banking simulator. Write a code in python that simulates the banking system.
#The program should:
# - be able to create new banks
# - store client information in banks
# - allow for cash input and withdrawal
# - allow for money transfer from client to client
#If you can think of any other features, you can add them.
#This code shoud be runnable with 'python task.py'.
#You don't need to use user input, just show me in the script that the structure of your code works.
#If you have spare time you can implement: Command Line Interface, some kind of data storage, or even multiprocessing.
#
#Try to expand your implementation as best as you can.
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository.
#
#Delete these comments before commit!
#Good luck.
from PyQt5.QtCore import QHistoryState


class Bank():
    def __init__(self):
        a=0

    def create_account(self, account_number, username, saldo, history):
        self.account_number = account_number
        self.saldo = saldo
        self.username = username
        self.history = history

        #return {"account number": self.account_number, "saldo": self.saldo, "username": self.username, "history": self.history}
        return account_number, saldo, username, history

    def cash_input(self, amount_of_money, username):
        username = self.username
        saldo = self.saldo + amount_of_money
        record= '+' + str(amount_of_money)
        history = self.history.append(record)

        return "Done, money added", username, saldo

    def cash_withdraw(self, amount_of_money,username):
        username = self.username
        if amount_of_money > self.saldo:
            return "you cant withdraw money, you're too poor"
        else:
            saldo = self.saldo - amount_of_money
            record = '-' + str(amount_of_money)
            hitory = self.history.append(record)

        return "Done, mone withdraw", username, saldo

    def trasfer_money(self, customer_giving, customer_recieving, ampunt):
        return "youre welcome"


if __name__ == '__main__':
    an_account = Bank()
    customer1 = an_account.create_account(2137, 'jkowalski', 1000000,[])
    customer2 = an_account.create_account(6969, 'amoczywas', 3030303, [])

    cash_input1 = an_account.cash_input(50, 'jkowalski')
    print(cash_input1)

    cash_withdraw1 = an_account.cash_withdraw(200000000000000, 'jkowalski')
    print(cash_withdraw1)

    cash_withdraw1 = an_account.cash_withdraw(200, 'jkowalski')
    print(cash_withdraw1)

    transfer1= an_account.trasfer_money('jkowalski', 'amoczywas', 1000)
    print(transfer1)


    #print(customer1)