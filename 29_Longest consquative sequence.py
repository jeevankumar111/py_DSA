def find_longest_continous(arr):
    arr.sort()
    n=len(arr)

    if n ==1:
        return 1

    count =1
    max_count=-1

    for  i in range(n -1):
        if arr[i+1] -arr[i] ==1:
            count+=1
        elif arr[i+1] - arr[i] ==0:
            continue

        else:
            count =1

        max_count = max(max_count,count)

    return max_count

arr = [0,1,1,1,1,1,2,3]
result = find_longest_continous(arr)
print("Longest consecutive subseqence ", result)
