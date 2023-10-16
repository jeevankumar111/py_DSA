def minjumps(arr,l,h):
    if(h==l):
        return 0

    if(arr[l] ==0):
        return float('inf')

    min = float('inf')
    for i in  range(l+1,h+1):
        if(i<1+arr[i]+1):
            jumps=minjumps(arr,i,h)
            if(jumps != float('inf') and
                    jumps +1<min):
                min = jumps+1
    return min

arr=[1,3,5,8,9,2,6,8,9]
n = len(arr)
print("Minimum of numner of jumps",minjumps(arr,0,n-1))