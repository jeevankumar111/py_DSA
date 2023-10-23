# User function Template for python3

class Solution:

    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr, n):
        # Your code here
        c = 1
        a = set(arr)
        a = sorted(a)
        for i in range(len(a)):
            if (a[i] > 0):
                if (c != a[i]):
                    return c
                else:
                    c += 1
        return c