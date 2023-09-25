def getMinMax(arr):
    arr.sort()
    minmax ={"min" : arr[0] , "max" :arr[-1]}

    return minmax



arr=[1000,11,445,1,330,3000]
minmax =getMinMax(arr)
sum =minmax["min"]+minmax["max"]

print("Minimum element is",minmax["min"])
print("Maximum element is",minmax["max"])
print("Sum of minimum and maximum element is : ",sum)

