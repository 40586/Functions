#Kieran burnett
#Functions 2 hoilday work
cake = "it's a lie"
import pdb

def selection_():
    print("Please choose using the number shown")
    print("1. Encryption")
    print("2. Decryption")
    selection = int(input(":"))
    if selection == 1:
        encryption()
    elif selection == 2:
        decryption()
    else:
        selection_()

def input_():
    word  = input("Please input the word: ")
    key = int(input("Please enter the key (0-25): "))
    if key <0 or key >25:
        input_()
    return word,key

def lists_letters(word,letters):
    count2 = 0
    count = 0
    while count != len(word):
        letters.append(word[count2:count2+1])
        count = count + 1
        count2 = count2 + 1
    return letters

def encrypt(count,letters,key):
    count2 = 0
    while count2 != count:
        letters[count2] = ord(letters[count2])
        letters[count2] = int(letters[count2]) + int(key)
        count2 = count2 + 1
    return letters

def decrypt(count,letters,key):
    count2 = 0
    while count2 != count:
        letters[count2] = ord(letters[count2])
        letters[count2] = int(letters[count2]) - int(key)
        count2 = count2 + 1
    return letters
        
def to_words(count,letters):
    count2 = 0
    while count2 != count:
        letters[count2] = chr(letters[count2])
        count2 = count2 + 1
    count2 = 0
    word = ""
    while count2 != count:
        word = word + letters[count2]
        count2 = count2 + 1
    return word
    
def out(word1,word,key):
    print(" Your en/decrypted word is: ",word1)
    print(" Your original word was: ",word)
    print(" Your key was: ",key)

def encryption():
    word1 = ""
    letters = []
    word,key = input_()
    count = len(word)
    letters = lists_letters(word,letters)
    letters = encrypt(count,letters,key)
    word1 = to_words(count,letters)
    out(word1,word,key)

def decryption():
    word1 = ""
    letters = []
    word,key = input_()
    count = len(word)
    letters = lists_letters(word,letters)
    letters = decrypt(count,letters,key)
    word1 = to_words(count,letters)
    out(word1,word,key)

def main():
    selection_()
    
main()
