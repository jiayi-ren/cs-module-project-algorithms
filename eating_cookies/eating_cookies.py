'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, number_of_ways = []):
    # Your code here
    # recursive:
    if n == 0 or n == 1:
        return 1
    elif n ==2:
        return 2
    elif n >= 3:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    else:
        return 0

    # for larget input
    # use a list to store all previous counts
    # number_of_ways = [0 for i in range(0, n + 1)] #
    # if n == 0 or n == 1:
    #     return 1
    # if n == 2:
    #     return 2 
    # # base cases 
    # number_of_ways[0] = 1
    # number_of_ways[1] = 1
    # number_of_ways[2] = 2
  
    # # Iterate for all values from 3 to n 
    # for i in range(3, n + 1): 
    #     number_of_ways[i] = number_of_ways[i - 1] + number_of_ways[i - 2] + number_of_ways[i - 3] 
      
    # return number_of_ways[n] 

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
