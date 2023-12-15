class Solution:
    def trappingWater(self, arr, n):
        # Code here
        low = 0
        high = n - 1
        ml = 0
        mr = 0
        ans = 0
        while (low <= high):
            if arr[low] < arr[high]:
                if arr[low] > ml:
                    ml = arr[low]
                else:
                    ans = ans+ml - arr[low]
                low += 1

            else:
                if arr[high] > mr:
                    mr = arr[high]
                else:
                    #to remove
                    ans = ans+mr - arr[high]
                high -= 1
        return ans
        
