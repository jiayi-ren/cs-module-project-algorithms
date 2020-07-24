'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # method 1: FAILED LARGE INPUT
    # create window array of size k with two pointers (start=0, end=k)
    # find max for each window array
    # iterate through nums until end reaches len(nums)-1
    # O(n^2)
    # start = 0
    # end = k
    # ans = []
    # while end <= len(nums):
    #     arr = nums[start:end]
    #     ans.append(max(arr))
    #     start +=1
    #     end +=1
    # return ans

    # method 2:
    # use
    if not nums:
        return []
    # check max number of first k elements
    #
    max_number = max(nums[:k])
    max_number_index = nums[:k].index(max_number)
    ans = [max_number]
    i = k
    # start at kth element till the end of nums
    for i in range(k, len(nums)):
        # bigger number appears
        if nums[i] > max_number:
            max_number, max_number_index = nums[i], i
        # max number is out of window
        elif i-(k-1) >= max_number_index:
            arr = nums[i-(k-1): (i+1)]
            max_number = max(arr)
            max_number_index = i-(k-1) + arr.index(max_number)
        ans.append(max_number)
    return ans


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
