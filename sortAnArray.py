class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(1, len(nums)):
            idx = nums[i]
            j = i - 1
            while j >= 0 and idx < nums[j]:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = idx
        return nums
