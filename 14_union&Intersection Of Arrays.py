def unionArray(arr1,arr2,n,m):
    set1 = set(arr1)
    set2 = set(arr2)

    result1 = list(set1.union(set2))
    return result1

def interscetionArray(arr1,arr2,n,m):
    set1 = set(arr1)
    set2 = set(arr2)

    result2 = list(set1.intersection(set2))
    return result2








if __name__ == "__main__":
    arr1 =[1,2,2,2,3]
    arr2 =[2,3,3,4,5,5]
    n = len(arr1)
    m= len(arr2)

    uni =unionArray(arr1,arr2,n,m)
    for i in uni:
        print(i,end=" ")

    inter = interscetionArray(arr1, arr2, n, m)
    for i in inter:
        print( "\n",i, end=" ")
