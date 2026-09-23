n=int(input("enter the range of array\n"))
arr=[]
for i in range(n):
     arr.append(int(input("Enter element: ")))
print(arr)
value =int(input("enter the value"))
low=0
high=n-1
mid=int(low+(low+high)/2)
while low<=high:
    if arr[mid]==value:
        print(mid)
        break
    elif arr[mid]>value:
        high=mid-1
    else:
        low=mid+1
    mid=int(low+(low+high)/2)
