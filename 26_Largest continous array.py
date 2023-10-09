from sys import maxsize


def maxsubarray(a,size):
    max_so_far = -maxsize - 1
    max_ending_here = 0

    for i in range(0,size):
        max_ending_here += a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here =0
    return max_so_far


a = [-2,-3,4,-1,1,5,-3]
print ("Maximum contiguos sum is",maxsubarray(a,len(a)))