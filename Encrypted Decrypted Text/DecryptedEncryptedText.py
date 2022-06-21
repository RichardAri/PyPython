
from turtle import numinput


letras = 'abcdefghijlmnñopqrstuvwxyz'

def encrypt(text):
    temp = ''
    numIndex = 0
    for letra in text:
        if letra in letras:
            numIndex = letras.find(letra) + 13
            if numIndex > len(letras):
                numIndex = numIndex - len(letras)
            elif numIndex < 0:
                numIndex = numIndex + len(letras)
            temp += letras[numIndex]
        else:
            temp += letra
    return temp

def decrypt(text):
    temp = ''
    numIndex = 0 
    for letra in text:
        if letra in letras:
            numIndex = letras.find(letra) - 13
            if numIndex < 0:
                numIndex = numIndex + len(letras)
            temp += letras[numIndex]
        else:
            temp += letra
    return temp

def main():
    text = ''
    while True:
        print('Welcome to Encrypted/Decrypted of Texts : ')
        msg = input('Input Text : ')
        opt = input('Selection e(encrypted) / d(decrypted)')

        if (text.upper == 'QUIT'):
            break
        
        if opt.startswith('e'):
            text = encrypt(msg)
        elif opt.startswith('d'):
            text = decrypt(msg)
        else:
            print('Invalid value ')
            text = ''
        print('\n')
        print(text)
        print('\n')

if __name__ == '__main__':
    main()