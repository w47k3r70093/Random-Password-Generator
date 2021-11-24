import random

characters = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

number = int(input("Number of passwords? --> "))
password_length = int(input("Password Length? --> "))

for i in range(number):
    password = ''
    for j in range(password_length):
        password += random.choice(characters)
    print(password)