# Input: numbers = [1,2,3,4], target = 3

# Output: [1,2]

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]

            if currSum > target:
                r -= 1
            elif currSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []

