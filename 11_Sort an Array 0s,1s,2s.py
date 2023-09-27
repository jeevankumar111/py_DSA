def sort012(arr,n):
    lo=0
    hi=n-1
    mi=0

    while mi<=hi:
        if arr[mi] ==0:
            arr[lo],arr[mi] = arr[mi],arr[lo]
            lo +=1
            mi +=1

        elif arr[mi] == 1:
            mi +=1

        elif arr[mi] ==2:
            arr[mi],arr[hi] = arr[hi],arr[mi]
            hi = hi-1

    return arr


def printArray(arr):
    for i in arr:
        print(i,end=' ')



arr = [1,2,1,0,2,1,2,0,2,1]
n = len(arr)
arr =sort012(arr,n)
print("The sorted array was : ")
printArray(arr)

