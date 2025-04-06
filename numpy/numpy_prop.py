import numpy as np
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
# print(arr[1, 2])      # 2nd row 3rd column
# for i in range(3):
#     print(arr[0, i])  # first row and another is arr[0,:]
# for i in range(3):
#     print(arr[i, 2]) # 3rd column arr[:,2]
# for i in range(2):
#     for j in  range(2):
#         print(arr[i, j]);   # arr[0:2,0:2]
# for i in range(3):
#     print(arr[2,i]);  # arr[2,:] all ele of 3rd row
# for i in range(3):
#     arr[i,1]=0;    # 2nd col with 0 arr[:,1]=0;   
# for i in range(3):
#     for j in range(3):
#         print(arr[i,j],end=" ");
#     print();
# for i in range(3):
#     for j in  range(3):
#         arr[i][j]=arr[i][j]*2;
#         print(arr[i][j],end=" ");
#     print();
    
    
    
# for i in range(3):
#     for j in  range(3):
#         if (arr[i][j]>10):
#             arr[i][j]=99;
#         print(arr[i][j],end=" ");
#     print();



# for i in range(3):
#     for j in  range(3):
#         arr[i][j]=arr[i][j]+50;
#         print(arr[i][j],end=" ");
#     print();




# arr2=np.array([5,10,15,20,25,30]);
# mx=-1;
# for i in range(6):
#     if(arr2[i]>mx):
#         mx=arr2[i];
# print("Max",mx);

# mi=1000;
# for i in range(6):
#     if(arr2[i]<mi):
#         mi=arr2[i];
# print("Min",mi);



# a=np.array([4,3,5,46,7,8]);
# b=a.copy();
# print(a is b);
# print(b is a);


ar=np.arange(1,17).reshape(4,4)

for i in range(4):
    for j in range(4):
        if(i==j):
            ar[i][j]=0;
for i in range(4):
    for j in range(4):
        print(ar[i][j],end=" ");
    print();
print();  
for i in range(4):
    for j in range(4):
        if(ar[i][j]>10):
            ar[i][j]=100;
for i in range(4):
    for j in range(4):
        print(ar[i][j],end=" ");
    print();