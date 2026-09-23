
n=int(input("enter the range of array\n"))
arr=[]
for i in range(n):
     arr.append(int(input("Enter element: ")))
print(arr)
value =int(input("enter the value"))
for i in range(n):
    if arr[i]==value:
     print(i)
     break