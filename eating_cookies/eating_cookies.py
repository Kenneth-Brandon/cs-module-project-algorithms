'''
Input: an integer
Returns: an integer
'''
# With the cache, every n value is now only computed once then saved to the cache
# Cache reduced the runtim from O(3^n) to O(n)
# Space complexity was increased by a decent margin, though


def eating_cookies(n, cache={}):
    # base case: if less than 0 then it's not a valid path
    # if 0, then this is a valid path to 0 cookies
    # (not that there is 1 way to eat 0 cookies, fyi)

    # in addition to lowering the number of base cases,
    # a huge improvement would be to add a cache
    # this way, the algorithm doesn't have to repeat
    # computations

    # initiate cache as a second param in the function as an empty dict
    # think of cache as state in react.js

    # check the cache before running any new computations
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in cache:
        # don't go on to recursion, just return previously made computation
        return cache[n]
    else:
        # run eating_cookies recursively and store the result in cache[n]
        cache[n] = eating_cookies(
            n-3, cache) + eating_cookies(n-2, cache) + eating_cookies(n-1, cache)
    # return what's stored in cache for that n value
    return cache[n]


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5
    # num_cookies = 3

    print(
        f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to eat {num_cookies} cookies")
