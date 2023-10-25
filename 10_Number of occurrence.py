def countOccurence(arr,n,x):
    count=0
    for i in range(n):
        if x == arr[i]:
            count +=1
    return count




arr =[1,22,44,66,88,8,8]
n=len(arr)
x =8

print("The number of Occurrences are : ",countOccurence(arr,n,x))
0000


