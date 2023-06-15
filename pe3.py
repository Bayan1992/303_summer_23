import string


def encode(input_text, shift):
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    input_text = input_text.lower()  # convert input text to lowercase
    output_text = ''

    for char in input_text:
        if char.isalpha():
            index = (alphabet.index(char) + shift) % len(alphabet)
            new_char = alphabet[index]
            output_text += new_char
        else:
            output_text += char

    return alphabet, output_text


def decode(input_text, shift):
    alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
    input_text = input_text.lower()  # convert input text to lowercase
    output_text = ''

    for char in input_text:
        if char.isalpha():
            index = (alphabet.index(char) - shift) % len(alphabet)
            new_char = alphabet[index]
            output_text += new_char
        else:
            output_text += char

    return output_text

# Recall the function

print(encode("A", 3))


# Class Exercise

import datetime


class BankAccount:
    def __init__(self, name="Clocks", ID="123", creation_date=datetime.date.today(), balance=0):
        if creation_date > datetime.date.today():
            raise Exception("Creation date cannot be in the future")
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount should be a positive number. No changes have been made to your balance."
        else:
            self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def view_balance(self):
        return self.balance


class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if (datetime.date.today() - self.creation_date).days < 180: # 180 days is roughly 6 months
            raise Exception("Cannot withdraw from a SavingsAccount within 6 months of creation")
        elif self.balance < amount:
            raise Exception("Cannot overdraft a SavingsAccount")
        else:
            self.balance -= amount


class CheckingAccount(BankAccount):
    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 30  # Overdraft penalty
        self.balance -= amount








