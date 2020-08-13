'''
Input: a List of integers
Returns: a List of integers
'''
# Check if the array exists
# Loop through the array
# If the value is zero...
# Remove the value
# Append it to the back of the array
# Return the properly-mutated array


def moving_zeroes(arr):
    # Your code here

    if arr:
        for i in arr:
            if i == 0:
                arr.remove(i)
                arr.append(i)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
