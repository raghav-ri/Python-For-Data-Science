# list1=[1,2,34,56,67];
# print(list1[3])
# print(list1[-3])
# print(list1[0:3])
# l2=[90,344,65,76]
# print([list1+l2])
# print(list1*2)


# create a dict consisting of name age and marks print the age of the students


# dict={"name":"Raghav","age":21,"marks":8.27}
# print(dict["age"])


# print(5&3)
# print(5|3)
# print(5^3)
# print(5>>2)
# print(5<<2)
# print(~5)
# print(~3)

# l1 = [1, 4, 5, 6]
# n2 = int(input("Enter the number: "))

# print(n2 in l1)
# l1=[1,2,3]
# l2=l1# in python assignment creates reference not copies and it is called chained assignment
# l3=[1,2,3]
# print(l1 is l2)
# print(l1 is l3)
# print(l3 is l2)
# print(id(l1))
# print(id(l2))
# print(id(l3))


# s1=int(input("Subject1 Marks:"))
# s2=int(input("Subject2 marks:"))
# s3=int(input("Subject3 marks:"))
# s4=int(input("Subject4 marks:"))
# s5=int(input("Subject5 marks:"))
# total=s1+s2+s3+s4+s5
# per=total/5
# print("Total marks: ",total)
# print("Percentage: ",per)

# n1=int(input("Enter the 4 digit number: "))
# n2=n1
# sum=0
# while(n2>0):
#     n3=n2%10
#     sum=sum+n3
#     n2=n2//10
# print(sum)

n2= int(input("Enter the 4 digit number: "))
n3=n2%10
sum=0
sum=sum+n3
n2=n2//10
n4=n2%10
sum=sum+n4
n2=n2//10
n5=n2%10
sum=sum+n5
n2=n2//10
n6=n2%10
sum=sum+n6
print(sum)