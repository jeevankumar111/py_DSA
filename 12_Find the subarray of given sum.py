def subArrauSum(arr,n,sum):
    for i in range(0,n):
        currentSum =arr[i]
        if(currentSum==sum):
            print("Sum found in the Indexes", i)
            return
        else:
            for j in range(i+1,n):
                currentSum = currentSum+ arr[j]
                if(currentSum == sum):
                    print("Sum found between indexes",i,"and",j)
                    return

    print("No Subarray Found")





arr =[13,55,33,6,22,11,7,4]
n = len(arr)
sum =39
subArrauSum(arr,n,sum)
