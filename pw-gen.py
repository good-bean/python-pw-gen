################################################################
# Project       : Password Generator                           #
# Program name  : pw-gen.py                                    #
# Author        : Bridget Flanery (good-bean)                  #
# Date created  : 20240718                                     #
# Purpose       : Create a password generator in Python that   #
#                 provides complexity required by most systems #
################################################################

# You will need to import pyperclip if you want the generated
# password to be copied to the clipboard automatically.
import random, pyperclip

def main():
    result = makePassword(18)
    print(result)
    pyperclip.copy(result)

def makePassword(length):
    password = ''

    for i in range(length - 2):
        password += randomCharacter('ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                                    'abcdefghijklmnopqrstuvwxyz'
                                    '0123456789+-*/?!@#$%&()')
    
    randomDigit = randomCharacter('0123456789')
    password = insertAtRandom(password, randomDigit)

    randomSymbol = randomCharacter('+-*/?!@#$%&()')
    password = insertAtRandom(password, randomSymbol)

    return password

def randomCharacter(characters):
    n = len(characters)
    r = int(random.randint(0, n-1))

    return characters[r:r+1]

def insertAtRandom(str, toInsert):
    n = len(str)
    r = int(random.randint(0, n+1))

    return str[0:r] + toInsert + str[r:]

if __name__ == '__main__':
    main()
