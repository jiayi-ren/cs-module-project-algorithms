'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache = []):
    # Your code here
    # recursive:
    # time: O(3^n)
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    elif n >= 3:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    else:
        return 0

    # time: O(3^n)
    # if n < 0:
    #     return 0
    # elif n == 0:
    #     return 1
    # else:
    #     return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    
    # add cache to save previous
    # if n < 0:
    #     return 0
    # elif n == 0:
    #     return 1
    # elif n in cache:
    #     return cache[n]
    # else:
    #     cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
    #     return cache[n]


    # for larget input
    # use a list to store all previous counts
    # time: O(n)
    # cache = [0 for i in range(0, n + 1)] #
    # if n == 0 or n == 1:
    #     return 1
    # if n == 2:
    #     return 2 
    # # base cases 
    # cache[0] = 1
    # cache[1] = 1
    # cache[2] = 2
  
    # # Iterate for all values from 3 to n 
    # for i in range(3, n + 1): 
    #     cache[i] = cache[i - 1] + cache[i - 2] + cache[i - 3] 
      
    # return cache[n] 

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
