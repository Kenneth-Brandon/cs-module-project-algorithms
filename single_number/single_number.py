'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
# Create a set
# Loop through the array
# If this iteration is in the set already, remove it
# Otherwise, it's a single value so add it
# Return the first value of the current set list
# There should only be one element


def single_number(arr):
    # Your code here

    s = set()

    for i in arr:
        if i in s:
            s.remove(i)
        else:
            s.add(i)
    return list(s)[0]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")
