'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    # method 1:
    # iterate through arr
    # if zero, swap with last non zero item

    start = 0
    end = len(arr)-1
    while start < end:
        if arr[start] == 0:
            while True:
                if arr[end] != 0:
                    arr[start], arr[end] = arr[end], arr[start]
                    end -= 1
                    break
                else:
                    end -=1
                if start == end:
                    return arr
        start+=1
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")