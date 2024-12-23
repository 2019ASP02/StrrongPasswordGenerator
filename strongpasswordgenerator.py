#include the library file 
import random # randomly generates the string
import string # include the string (Charactor, Numbers and symbols)

#initilize the strings
#ch1 = list(string.ascii_lowercase)
#ch2 = list(string.ascii_uppercase)
#ch3 = list(string.ascii_letters)
pun = list(string.punctuation)
#num = list(string.digits)

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
lc = len(str(cod)) # lenght of number
remaininglength = lgt - lw - lc  # calculate the lenght to add extra charator
#print(remaininglength)
# make it the list type
wrd = list(wrd)

spg = '' # stong password variable
binary = '01'
for i in range(0,lw-1,1):
    n = int(random.choice(binary))
    ow = wrd[i]
    nw = ow.upper() if n == 1 else ow.lower()
    wrd[i] = nw
processedword = ''.join(wrd)

if remaininglength > 1:
    fs = random.choice(pun) # first symbol it's exist first of the password
    ms = random.choices(pun,k=remaininglength-2) # middle symbols it's exist middle of the password
    ls = random.choice(pun) # last symbol it's exist last of the password
else:
    fs = random.choice(pun) # first symbol it's exist first of the password
    ms = ''
    ls = random.choice(pun) # last symbol it's exist last of the password

'''
#checking
print(fs)
print(processedword)
print(ms)
print(cod)
print(ls)
'''

# join the parts of the password 
spg = f"{fs}{processedword}{ms}{cod}{ls}"

#print the generated password
print("Strong Password : ",spg)