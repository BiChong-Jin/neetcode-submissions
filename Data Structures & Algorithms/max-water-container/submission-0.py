class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right, left = 0, len(heights) - 1
        res = 0

        while right < left:
            curr_contain = (left - right) * min(heights[right], heights[left])
            res = max(res, curr_contain)
            if heights[right] <= heights[left]:
                right += 1
            
            else:
                left -= 1


        return res