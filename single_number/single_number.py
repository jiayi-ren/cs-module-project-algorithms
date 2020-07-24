'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # method 1:
    # iterate through arr, create list with non duplicates
    # time: O(n^2), space:O(n)
    # no_duplicate = []
    # for i in arr: #O(n)
    #     if i in no_duplicate:
    #         no_duplicate.remove(i) #O(n)
    #     else:
    #         no_duplicate.append(i) #O(n)
    # return no_duplicate[0]

    # method 2:
    # iterate through, count number of occurrence
    # time: O(n^2), space: O(1)
    # for i in arr:
    #     if arr.count(i) == 1: #O(n)
    #         return i

    # method 3:
    # use dictionary, set
    # time: O(n), space: O(n)
    s = set()
    for i in arr: #O(n)
        if i in s: #O(1)
            s.remove(i) #O(1)
        else:
            s.add(i) #O(1)
    return s.pop()
    

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")