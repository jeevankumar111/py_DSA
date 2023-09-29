def find_duplicate(arr,n):
    duplicates =[]

    for i in  range(n):
        index = arr[i] % n
        arr[index] +=n

    for i in range(n):
        if arr[i] // n>=2:
            duplicates.append(i)
    return duplicates



arr = [1,6,3,1,3,6,6,7]
n = len(arr)
print("The reapeatingelements are")
ans = find_duplicate(arr,n)
for i in ans:
    print(i,end=" ")
