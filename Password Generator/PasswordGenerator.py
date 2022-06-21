import random

characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

def passwordGenerator(length=8):
    if (length>=length):
        temp = ''
        num = 0
        lengthChar = len(characters)-1
        while num < length:
            rnd = random.randint(0,lengthChar)
            temp += characters[rnd]
            num += 1
        return temp
    else:
        return 'Min length 8'
    

print('Welcome to password generator : ')

length = int(input('Insert Length : '))

print('Password : ')
print(passwordGenerator(length))

        
