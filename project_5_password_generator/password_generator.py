import random

letter_list = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
    ]

symbol_list = [
    '!',
    '@',
    '£',
    '$',
    '%',
    '^',
    '&',
    '*',
    '(',
    ')',
    '-',
    '_',
    '+',
    '[',
    ']',
    '?',
]



print("Welcome to the PyPassword Generator")
letters = input("How many letters would you like in your password?\n")
numbers = input("How many numbers would you like?\n")
symbols = input("How many symbols would you like?\n")

password_elements = []

for i in range(int(letters)):
    choice = random.choice(letter_list)
    to_upper = random.randint(0,1)
    if to_upper:
        choice = choice.capitalize()
    password_elements.append(choice)

for i in range(int(numbers)):
    password_elements.append(str(random.randint(0,9)))

for i in range(int(symbols)):
    choice = random.choice(symbol_list)
    password_elements.append(choice)

# print(password_elements)
random.shuffle(password_elements)
# print(password_elements)

new_password = ''
for i in password_elements:
    new_password += i


print(f'Your password is: {new_password}')