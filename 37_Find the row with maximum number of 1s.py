class Solution:

    def rowWithMax1s(self, arr, n, m):
        # code here
        target = 0
        max_count = 0
        for i in range(n):
            count = 0
            for j in range(m):
                if arr[i][j] == 1:
                    count += 1
            if count > max_count:
                max_count = count
                target = i
            else:
                continue
        if max_count == 0:
            return -1
        return target
