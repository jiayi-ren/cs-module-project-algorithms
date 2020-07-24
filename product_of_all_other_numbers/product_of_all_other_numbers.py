'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # Your code here
    # method 1:
    # iterate using index
    # use another pointer iterate through the list
    # if both pointers are not equal, multiply
    # time: O(n^2), space: O(n)
    # product_list = []
    # for i in range(0, len(arr)): #O(n)
    #     j = 0
    #     ans = 1
    #     while j <= len(arr)-1: #O(n-1)
    #         if j != i:
    #             ans = ans * arr[j]
    #         j += 1
    #     product_list.append(ans)

    # return product_list

    # method 2:
    # loop through arr, calculate product of all left elements
    # loop through arr, calculate product of all right elements
    # multiply left and right
    # time: O(n), space: O(n)
    ans = [0]*len(arr)
    left = [0]*len(arr)
    right = [0]*len(arr)
    left[0] = 1 # no left elements from first index
    right[len(right)-1] = 1 # no right elements from last index
    # calculate product of all left elements
    for i in range(1, len(arr)):
        left[i]=arr[i-1]*left[i-1]
    # calculate product of all right elements
    for i in range(len(arr)-2, -1, -1):
        right[i]=arr[i+1]*right[i+1]
    # multiply left and right
    for i in range(len(ans)):
        ans[i] = left[i]*right[i]
    return ans

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
