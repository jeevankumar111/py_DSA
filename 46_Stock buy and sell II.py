
from typing import List


class Solution:
    def stockBuyAndSell(self, n : int, prices : List[int]) -> int:
        # code here
        profit = 0
        left, right = 0, 1
        while right < n:
            if prices[left] < prices[right]:
                profit =profit+  prices[right]-prices[left]
                left=left+1
            else:
                left = right
            right=right+1
        return profit