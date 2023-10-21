def findnumbers(arr,n,sum):
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k] == sum:
                    print("TRIPLET is",arr[i],
                          ",",arr[j],",",arr[k])
                    return True

    return False

arr =[1,4,45,6,10,8]
sum =22
n = len(arr)
findnumbers(arr,n,sum)
00
