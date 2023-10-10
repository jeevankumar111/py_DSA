def findMin(arr,n):
    min_ = arr[0];


    for i in range(n):
        if arr[i]<min_:
            min_ =arr[i]
    return min_;


arr=[2,4,2,3222,3,1]
n =  len(arr)
print(findMin(arr,n))