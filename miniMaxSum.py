def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    sum1 = 0
    sum2 = 0
    for i in arr[:-1]:
        sum1 = sum1 + i
       
    for j in arr[1:]:
        sum2 = sum2 + j
    
    print(sum1, sum2)
    
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    
    
#     sample input
#     1 2 3 4 5


# output
# 10 14
