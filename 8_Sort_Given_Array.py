arr=[1,4,6,6,777,44,33]
temp=0
max_size =len(arr)
print("The elements of array before we sorted : ");
for i in range(0,max_size):
    print(arr[i],end=" ")

for i in range(0,max_size):
    for j in range(i+1,max_size):
        if(arr[i]>arr[j]):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j] =temp
print("\nThe elements after sorted : ")

for i in range(0,max_size):
    print(arr[i],end=" ")



