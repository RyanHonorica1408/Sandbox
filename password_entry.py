"""
CP1404/CP5632 - Practical 3
Password checker
"""
MIN_LENGTH = 2
MAX_LENGTH = 6
password = input("Input Valid Password. Must be between {} and {} characters long:".format(MIN_LENGTH, MAX_LENGTH))
if len(password) < MIN_LENGTH:
    password = input("Input Valid Password. Must be between {} and {} characters long:".format(MIN_LENGTH, MAX_LENGTH))
else:
    print('*' * len(password))


