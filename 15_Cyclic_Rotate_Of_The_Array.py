def rotateArray(arr,n):
   i =0
   j =n-1
   while i!=j:
       arr[i],arr[j] = arr[j],arr[i]
       i +=1
   pass


arr=[1,2,3,4,5]
n =len(arr)

n = len(arr)
print("Given array is")
for i in range(0, n):
    print(arr[i], end=' ')

rotateArray(arr, n)

print("\nRotated array is")
for i in range(0, n):
    print(arr[i], end=' ')