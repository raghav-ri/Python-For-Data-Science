# n1=int(input("Enter the number: "))
# if(n1%2==0):
#     print("Even")
# else:
#     print("Odd")

# n1=int(input("Enter the number 1: "))
# n2=int(input("Enter the number 2: "))
# n3=int(input("Enter the number 3: "))
# if(n1>n2 and n1>n3):
#     print(n1,"is the largest number")
# elif(n2>n1 and n2>n3):
#     print(n2,"is the largest number")
# else:
#     print(n3,"is the largest among three")

# import math
# a=int(input("Enter a: "))
# b=int(input("Enter b: "))
# c=int(input("Enter c: "))
# d = sqrt(b**2 - 4*a*c)
# if(d>0):   
#     root1 = (-b + d) / (2*a)
#     root2 = (-b - d) / (2*a)
#     print("Root1: ",root1)
#     print("Root2: ",root2)
# elif(d==0):
#     root = -b / (2*a)
#     print("Root1 == Root2 and root is ",root)
# else:
#     print("Root are not real ")

 
# c=input("Enter the character: ")
# if(c=="A" or c=="a" or c=='E' or c=="e" or c=="I" or c=="i" or c=="O" or c=="o" or c=="U" or c=="u"):
#     print("Vowel")
# else:
#     print("Consonant")


       #FACTORIAL
    
# n1=int(input("Enter the number: "))
# n2=1
# while(n1>=1):
#     n2=n2*n1
#     n1=n1-1
# print(n2)



      #TABLE


n1=int(input("Enter the number: "))
for i in range (1 , 11):
# print(n1,"*",i,"=",n    1*i)  #print(n1*i)
    print(f"{n1} * {i} = {n1*i}")

