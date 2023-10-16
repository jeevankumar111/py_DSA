def calculatespan(price,n,s):
    s[0] =1
    for i in range(1,n,1):
        s[i] =1

        j =i-1
        while(j>=0) and (price[i] >= price[j]):
            s[i] +=1
            j -=1
def printArray(arr,n):
    for i in range(n):
        print(arr[i],end=" ")



price=[10,4,5,90,120,80]
n = len(price)
s=[None]*n
calculatespan(price,n,s)

printArray(s,n)