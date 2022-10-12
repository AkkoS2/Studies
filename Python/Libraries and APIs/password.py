# bibliotecas
import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbols = '`!@#$%^&*()_-+={[}]|\:;"<,>.?/'

length = random.randint(8, 16)
everything = lower + upper + number + symbols
password = ''.join(random.sample(everything, length))

print(password)

# This is a simple password generator, made with the purpose of studying
# Python's random library and simple string manipulation
