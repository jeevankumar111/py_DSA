def firstRepeat(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                return i

    return -1
if __name__ == '__main__':
        arr = [2,1,2,3,4,5,7,9]
        n =len(arr)
        jk=firstRepeat(arr,n)

        if jk == -1:
            print("No repeating element found")
        else:
            print("First reeating element is",arr[jk])



