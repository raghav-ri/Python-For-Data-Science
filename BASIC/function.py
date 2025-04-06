# def swap(n1,n2):
#     n3=n1
#     n1=n2
#     n2=n3
#     print("N1 is ",n1)
#     print("N2 is ",n2)

    
# n1=int(input("Enter first number "))
# n2=int(input("Enter second number: "))
# swap(n1,n2)


# def add(n1,n2):
#     n3=n1+n2
#     return n3
# def subs(n1,n2):
#     n3=n1-n2
#     return n3
# def multiply(n1,n2):
#     n3=n1*n2
#     return n3
# def div(n1,n2):
#     n3=n1/n2;
#     return n3
# p1=add(2,3)
# p2=subs(8,4)
# p3=multiply(7,2)
# p4=div(64,8)
# print("Addition: ",p1)
# print("Subtraction: ",p2)
# print("Multiplication: ",p3)
# print("Division: ",p4)



# def calculate_all(n1, n2):
#     addition = n1 + n2
#     subtraction = n1 - n2
#     multiplication = n1 * n2
#     division = n1 / n2
#     return addition, subtraction, multiplication, division
# n1 = int(input("Enter first number: "))
# n2 = int(input("Enter second number: "))
# results = calculate_all(n1, n2)
# print("Addition: ", results[0])
# print("Subtraction: ", results[1])
# print("Multiplication: ", results[2])
# print("Division: ", results[3])



# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# result = factorial(4)
# print("Factorial:", result)

def fibonacci(n):
    n=0
    n1=1
    n2=n+n1
    n=n1
    n1=n2
    for i in range(2,n):
        n=n1+n2
        n2=n1
        n1=n
        return n1
print(fibonacci(10))
       
