def kthSmallest(arr,n,k):
    arr.sort()
    return arr[k-1]

if __name__ == '__main__':
    arr = [12,3,5,6,7,19]
    n= len(arr)
    k=6

    print("Kth smallest element is ",kthSmallest(arr,n,k))