"""
Given a sorted array of integers, return the indices
of two elements (in different positions) that sum up
to the target value. Assume there is exactly one solution
O(n)
"""
nums = [-1, 2, 3, 4, 7, 9] 

def targetSum(nums, target):
    L, R = 0, len(nums) -1
    while L < R:
        if nums[L] + nums[R] > target:
            R -= 1
        elif nums[L] + nums[R] < target:
            L += 1
        else:
            return [L, R]