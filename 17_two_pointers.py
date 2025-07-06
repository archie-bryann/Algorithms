# https://www.youtube.com/watch?v=cQ1Oz4ckceM

def two_sum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        cur_sum = numbers[l] + numbers[r]

        if cur_sum > target:
            r -= 1
        elif cur_sum < target:
            l += 1
        else:
            # return [numbers[l], numbers[r]]
            return [l + 1, r + 1]
    return []

print(two_sum([1,2,4,5,6,7,8,9,10], 15))