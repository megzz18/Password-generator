import random
letters=[ 'A','B','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','&','(',')','*','+']
print("welcome to password generator!")
n_letters=int(input("How many letters ypu want in your password?\n"))#4
n_symbols=int(input("How many symbols ypu want in your password?\n"))
n_numbers=int(input("How many numbers ypu want in your password?\n"))
password_List=[]
for i in range (1,n_letters+1):
    char=random.choice(letters)
    password_List+=char
for i in range (1,n_symbols+1):
    char=random.choice(symbols)
    password_List+=char
for i in range (1,n_numbers+1):
    char=random.choice(numbers)
    password_List+=char
print(password_List)
random.shuffle(password_List)
print(password_List)
password=""
for char in password_List:
    password+=char
print(password)

