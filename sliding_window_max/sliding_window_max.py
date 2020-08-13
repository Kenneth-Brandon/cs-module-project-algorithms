'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# Check if numbers array exists
# Set an empty list for the max numbers to live
# Loop through the list of numbers
# If k is <= the length of the numbers list
# Set the window to start at the current index and
# end 'k' elements over
# Move the window up one position
# Append the max number to the max_numbers array


def sliding_window_max(nums, k):
    # Your code here

    if nums:
        max_numbers = []
        for i in range(len(nums)):
            if k <= len(nums):
                window = nums[i:k]
                k += 1
                max_numbers.append(max(window))
    return max_numbers


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(
        f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
