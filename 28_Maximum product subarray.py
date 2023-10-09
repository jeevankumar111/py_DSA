def maxsubarray(arr):
    r=arr[0]

    imax =r
    imin =r

    for i in range(1,len(arr)):

        if arr[i] <0:
            imax,imin = imin,imax


        imax=max(arr[i],imax*arr[i])
        imin =min(arr[i],imin*arr[i])

        r=max(r,imax)

    return r

arr = [1,-2,-3,0,7,-8,-2]
print("Maximum Subarray product is", maxsubarray(arr))
