n=int(input("enter the range of array\n"))
arr=[]
for i in range(n):
     arr.append(int(input("Enter element: ")))
print(arr)
for i in range(n):
    for j in range (n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("sorted file: ",arr)
