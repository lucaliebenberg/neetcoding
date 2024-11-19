# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, j in enumerate(nums):
            diff = target - j
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[j] = i
        return
