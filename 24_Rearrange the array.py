class Solution:
    def rearrange(self, arr, n):
        # code here
        arr1 = []
        arr2 = []
        for i in range(0, len(arr)):
            if arr[i] >= 0:
                arr1.append(arr[i])
            else:
                arr2.append(arr[i])
        if len(arr1) >= len(arr2):

            for i in range(0, len(arr2)):
                arr[2 * i + 1] = arr2[i]
                arr[2 * i] = arr1[i]
            arr = arr[:2 * len(arr2)] + arr1[len(arr2):]

        else:

            for i in range(0, len(arr1)):
                arr[2 * i + 1] = arr2[i]
                arr[2 * i] = arr1[i]

            arr = arr[:2 * len(arr1)] + arr2[len(arr1):]
        return arr




n = 10
arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
