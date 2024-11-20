# Input: height = [1,7,2,5,4,7,3,6]

# Output: 36

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l,r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(area, res)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res
