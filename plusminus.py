
# Python program to do plusminus
Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with 6  digits after the decimal. The function should not return a value.

#Day1



def plusMinus(arr):
    # Write your code here
    p = 0
    n = 0
    z = 0   
    for i in arr:    
        if i>=1:
            p = p + 1
        elif i<0:
            n = n + 1
        else:
            z = z + 1
    pos = p/len(arr)
    neg = n/len(arr)
    zeo = z/len(arr)
    print("{:.6f}".format(pos))
    print("{:.6f}".format(neg))
    print("{:.6f}".format(zeo))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
