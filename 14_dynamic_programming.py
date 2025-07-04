# Writing a program to return the nth number in a fibonacci sequence
# Steps one can take to solve a problem with dynamic programming: Recursion, Store (Memoize), Bottom-up

# Recursion
def fib1(n): # Exponential run time
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib1(n-1) + fib1(n-2)
    return result

# Memoized Solution (concept)
def fib2(n, memo): # T(2n + 1) O(1)
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib2(n - 1, memo) + fib2(n - 2, memo)
    memo[n] = result
    return result

def fib2_memo(n):
    memo = [None] * (n + 1)
    return fib2(n, memo)

# Bottom-Up Approach
def fib3(n):  # O(n)
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n + 1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n + 1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
    return bottom_up[n]


if __name__ == "__main__":
    print(fib1(5))
    print(fib2_memo(100))
    print(fib3(1000))

# https://www.youtube.com/results?search_query=dynamic+programming