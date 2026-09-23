n=int(input("enter the range of array\n"))
arr=[]
for i in range(n):
     arr.append(int(input("Enter element: ")))
print(arr)
for i in range(n):
    mini=i
    for j in range(i+1,n):
        if arr[j]<arr[mini]:
           mini=j
    temp=arr[i]
    arr[i]=arr[mini]
    arr[mini]=temp
print("sorted array",arr)