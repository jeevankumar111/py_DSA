def pairs(arr,n,k):
    count =0
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i]+arr[j] ==k:
                count +=1
    return count



arr =[1,5,7,-1]
n = len(arr)
k=6
sum=pairs(arr,n,k)
print("Count of pairs is ",sum)