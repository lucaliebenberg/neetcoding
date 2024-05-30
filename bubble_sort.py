class Solution(object):
    """
    Bubble Sort algorithm implementation
    """
    def bubbleSort(self, nums):
        swapped = False
        while swapped:
            for i in range(nums):
                if nums[i] > nums[i+1]:
                    temp: nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = nums[i]
                    swapped = True
