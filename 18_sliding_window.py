# https://www.youtube.com/watch?v=jM2dhDPYMQM

def find_subarrays_with_sum(arr, target):
    result = []
    left = 0
    current_sum = 0

    for right in range(len(arr)):
        # Expand window by adding current element
        current_sum += arr[right]

        # Shrink window from left while sum is greater than target
        while current_sum > target and left <= right:
            current_sum -= arr[left]
            left += 1

        # If we found a valid subarray
        if current_sum == target:
            result.append(arr[left:right+1])
            # Move left pointer to find the next possible subarray
            current_sum -= arr[left]
            left += 1

    return result

print(find_subarrays_with_sum([1, 7, 4, 3, 1, 2, 1, 5, 1], 7))


def find_subarrays_with_sum_fixed_window(arr, target, k=2):
    result = []

    # Edge case: if array is smaller than window size
    if len(arr) < k:
        return result

    # Calculate sum of first window
    current_sum = sum(arr[:k])

    # Check if first window matches target
    if current_sum == target:
        result.append(arr[:k])

    # Slide the window through the rest of the array
    for i in range(k, len(arr)):
        # Remove leftmost element and add new rightmost element
        current_sum = current_sum - arr[i - k] + arr[i]

        # Check if current window matches target
        if current_sum == target:
            result.append(arr[i - k + 1:i + 1])

    return result


# Test with the same array
print(find_subarrays_with_sum_fixed_window([1, 7, 4, 3, 1, 2, 1, 5, 1], 7, k=2))