class Solution:

    def maxPathSum(self, arr1, arr2, m, n):

    sum1, sum2 = 0, 0

    max_sum = 0

    i, j = 0, 0

    while i < m and j < n:

        if arr1[i] < arr2[j]:

            sum1 += arr1[i]

            i += 1

            elif arr2[j] < arr1[i]:

            sum2 += arr2[j]

            j += 1

        else:

            sum1 += arr1[i]

    sum2 += arr2[j]

    max_sum += max(sum1, sum2)

    sum1 = 0

    sum2 = 0

    i += 1

    j += 1


if i == m:

    while j < n:
        sum2 += arr2[j]

        j += 1

    max_sum += max(sum1, sum2)

elif j == n:

    while i < m:
        sum1 += arr1[i]

        i += 1

    max_sum += max(sum1, sum2)

else:

    max_sum += max(sum1, sum2)

return max_sum
00000000
