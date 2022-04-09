#importing random
import random

#Defining characters available in different lists:
Alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numb=['1','2','3','4','5','6','7','8','9','0']
splch=['!','@','#','$','%','^','&','*','_']

#Func for startscreen:
def stsc():
    print("Enter 1 to know how it works")
    print("Enter 2 to get your new password")
    x=int(input())
    if x==1:
        how()
    elif x==2:
        userinput()
    else:
        print("Enter either 1 or 2 only!")
        stsc()

#Func to give info about how this works
def how():
    print("->This programs uses the random module.")
    print("->Based on the user input, the required number of characters are taken by the computer")
    print("->These characters are arranged randomly to create a password")
    userinput()

#Func to get inputs
def userinput():
    alphanoUC=int(input("\nEnter the number of Upper-case letters required:"))
    alphanoLC=int(input("Enter the number of Lower-case letters required:"))
    numbno=int(input("Enter the number of numerical characters required:"))
    splchno=int(input("Enter the number of special characters required:"))
    pasgen(alphanoUC,alphanoLC,numbno,splchno)

def pasgen(alphanoUC,alphanoLC,numbno,splchno):
    password=""
    i=1
    lst=[1,2,3,4]
    totalchar=alphanoUC+alphanoLC+numbno+splchno
    while i<=totalchar:
        y=random.choice(lst)
        if y==1:
            password=password+random.choice(Alpha)
        if y==2:
            password=password+random.choice(alpha)    
        if y==3:
            password=password+random.choice(numb)
        if y==4:
            password=password+random.choice(splch)
        i=i+1
    lst.remove(y)
    print("Password=",password)

#Beginning
print("Welcome to Password Generator")
stsc()

#----------Don't mind the code below----------
# #Uppercase
# def Alphafunc(alphanoUC,password,i):
#     while i>=alphanoUC:
#         password=password+random.choice(Alpha)
#         i=i+1
#     return password

# #Lowercase
# def alphafunc(alphanoLC,password,i):
#     while i>=alphanoLC:
#         password=password+random.choice(alpha)
#         i=i+1
#     return password

# #Numbers
# def numbfunc(numbno,password,i):
#     while i>=numbno:
#         password=password+random.choice(numb)
#         i=i+1
#     return password

# #Spl char
# def splchfunc(splchno,password,i):
#     while i>=splchno:
#         password=password+random.choice(splch)
#         i=i+1
#     return password

# #Func that generates the password and displays it
# def pasgen(alphanoUC,alphanoLC,numbno,splchno,password):
#     lst=[1,2,3,4]
#     y=1
#     i=1
#     while y<=4:
#         z=random.choice(lst)
#         print(lst,"\n",z)
#         if z==1:
#             password=password+Alphafunc(alphanoUC,password,i)
#         if z==2:
#             password=password+alphafunc(alphanoLC,password,i)
#         if z==3:
#             password=password+numbfunc(numbno,password,i)
#         if z==4:
#             password=password+splchfunc(splchno,password,i)
#         lst.remove(z)
#         y=y+1
#     print("Your high-security password is:\n",password)
