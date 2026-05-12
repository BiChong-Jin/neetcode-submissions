class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        if not nums:
            return False

        for num in nums:
            hashset.add(num)

        return True if len(hashset) != len(nums) else False