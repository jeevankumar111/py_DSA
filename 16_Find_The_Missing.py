def  findMissing(arr,n):
    #n*(n+1)/2
    expected_sum = n*(n+1)/2
    actual_sum= sum(arr)
    return int(expected_sum-actual_sum)






if __name__ == "__main__":
    arr =[]
    n =int(input("Enter the length of the array : "))

    for i  in range(n-1):
        m = int (input("Enter the element/number : "))
        arr.append(m)

    missing =findMissing(arr,n)
    print("The missing is {}".format(missing))
