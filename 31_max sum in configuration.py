import sys

def maxsum(arr,n):
    res = -sys.maxsize

    for i in range(0,n):
        cur_sum=0

        for j in range(0,n):
            index = int((i+j)%n)
            cur_sum += j*arr[index]
        res = max(res,cur_sum)
    return res

arr =[8,3,1,2]
n = len(arr)
print(maxsum(arr,n))