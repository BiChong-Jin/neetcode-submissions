class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        nums = [1, 2, 4, 6]
        prefix_mult = [1, 1, 2, 8]
        suffix_mult = [48, 24, 6, 1]

        res = []
        """

        prefix_mult = []
        suffix_mult = []
        res = []

        for idx, element in enumerate(nums):
            if idx == 0:
                prefix_mult.append(1)
            else:
                curr_prefix_mult = prefix_mult[idx - 1] * nums[idx - 1]
                prefix_mult.append(curr_prefix_mult)
        
        nums.reverse()
        for idx, element in enumerate(nums):
            if idx == 0:
                suffix_mult.append(1)
            else:
                curr_suffix_mult = suffix_mult[idx - 1] * nums[idx - 1]
                suffix_mult.append(curr_suffix_mult)
        
        suffix_mult.reverse()

        return [a * b for a, b in zip(prefix_mult, suffix_mult)]