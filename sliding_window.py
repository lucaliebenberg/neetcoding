"""
Sliding Window

Q: Given an array, return true if there
    are two elements within a window of
    size k that are equal
"""
# Check if array contains a pair of duplicate values,
# where the two duplicates are no farther than k positions
# from eachother (i.e -> arr[i] == arr[j] and abs(i - j) <= k)
# O(n * k)

nums = [1, 2, 3, 2, 3, 3]

def closeDuplicatesBruteForce(nums, k):
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False


# Same problem as above, but using sliding window
# O(n)
def closeDuplicates(nums, k):
    window = set() # Cur window of size <= k
    L = 0

    for R in range(len(nums)):
        if R - L + 1 > k:
            window.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    
    return False


"""
Q: Find the length of the longest
    subarray, with the same value
    in each position: O(n)
"""
def longestSubarray(nums):
    length = 0
    L = 0

    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R
        length = max(length, R - L + 1)
    return length


"""
Q: Find the minimum length subarray,
    where the sum is greater than or equal
    to the target. Assume all values are 
    positive: O(n)
"""
def shortestSubarray(nums, target):
    L, total = 0,0
    length = float("inf")

    for R in range(len(nums)):
        total += nums[R]
        while total >= target:
            length = min(R - L + 1, length)
            total -= nums[L]
            L += 1
    return 0 if length == float("inf") else length