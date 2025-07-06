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