#!/usr/bin/env python3
"""Simple cipher encrypter and decrypter.
Currently supports Caesar Ciphers (a simple shift cipher) and ROT47!"""

import argparse
import textwrap

def caesarCipher(message,key):
    #Simple Caesar Cipher -> Shifts the characters in the message by the key value
    result = ""

    for symbol in message:
        if (symbol.isupper()):
            result +=chr((ord(symbol) + key - 65) % 26 + 65)
        elif (symbol.islower()):
            result += chr((ord(symbol) + key - 97) % 26 + 97)
        else: #If not a letter
            result += symbol       
    return result

def rot47(message):
    #ROT47 Cipher -> Uses a larger library of symbols (ASCII) to encode data. Includes 94 ASCII characters. Shifts by 47
    result = ""

    for symbol in message:
        asciiValue = ord(symbol)
        if asciiValue >= 33 and asciiValue <= 126: #If within the range of 33-126 (ROT47 letters)
            result += chr(33 + ((asciiValue + 14) % 94))
        else:
            result+= symbol
    return result

# Use the argparse module to create a command line interface. 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Simple command line cipher tool! Currently supports encrypting and decrypting Caesar ciphers and ROT47',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example
            SimpleCiphers.py -c caesar -m encrypt -k 5 "This is a message to encrypt" # Encodes the message using the Caesar cipher with a key of 5.
            SimpleCiphers.py -c rot47 "This is a message to encrypt" # Encodes the message using ROT47
            ''')) 
    parser.add_argument('-c', '--cipher', choices=['caesar','rot47'], required=True, type = str.lower, help = 'Selects what cipher type to use!')
    parser.add_argument('-m', '--mode', choices=['encrypt', 'e', 'd', 'decrypt'], type = str.lower, help = 'Selects the mode (Encrypt or decrypt)')
    parser.add_argument('-k', '--key', help='Specify the key to use to encrypt / decrypt if applicable')
    parser.add_argument('input', nargs='?', type=str, help='The input to encrypt or decrypt, using the chosen cipher type and key.')
    args = parser.parse_args()

    if args.cipher == 'caesar':
        try:
            args.key = int(args.key)
            if not args.mode:
                raise Exception('No mode selected.')
            elif args.mode == 'encrypt' or 'e':
                result = caesarCipher(args.input,(args.key))
                print(result)
            elif args.mode == 'decrypt' or 'd':
                result = caesarCipher(args.input,(args.key) * -1)
                print(result)

        except:
            print("Unexpected input; refer to documentation. \n")
            print(parser.epilog)

    if args.cipher == 'rot47':
        try:
            result = rot47(args.input)
            print(result)
        except:
            print("Unexpected input; refer to documentation. \n")
            print(parser.epilog)
        
