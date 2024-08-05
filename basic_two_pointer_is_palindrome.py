"""
Given a string of characters, 
return true if it's a palindrome,
# return false otherwise: O(n)
"""
nums = [1,2,7,7,2,1]

def isPalindrome(nums):
    L, R = 0, len(nums)

    while L < R:
        if nums[L] != nums[R]:
            return False
        L += 1
        R -= 1
    return True
