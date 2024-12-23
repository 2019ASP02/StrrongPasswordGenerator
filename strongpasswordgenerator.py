#include the library file 
import random # randomly generates the string
import string # include the string (Charactor, Numbers and symbols)

#initilize the strings
ch1 = list(string.ascii_lowercase)
ch2 = list(string.ascii_uppercase)
ch3 = list(string.ascii_letters)
pun = list(string.punctuation)
num = list(string.digits)

#print(ch1)
#rint(ch2)
#print(ch3)
#print(pun)
#print(num)

# input take from User 
wrd = input("Enter a word that exist in password : ")  # user wish to put the word that exist in password
cod = int(input("Enter the number that exist in password : ")) # user wish to put the nummber that exist in password
lgt = int(input("Enter the total lenght(greater than lenght of entered word and number) : ")) # Total lenght of the password

lw = len(wrd) #lenght of word 
lc = len(cod) # lenght of number
lgt = lgt - lw - lc  # calculate the lenght to add extra charator

wrd = list(wrd)
cod = list(cod)

spg = '' # stong password variable
binary = '01'
for i in range(0,lw-1,1):
    n = int(random.choice(binary))
    ow = wrd[i]
    nw = ow.upper() if n == 1 else ow.lower()
    wrd[i] = nw


fs = random.choice(pun) # first symbol it's exist first of the password
