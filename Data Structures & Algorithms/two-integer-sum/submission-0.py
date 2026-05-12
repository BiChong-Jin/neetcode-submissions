class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return False
        #: Map[int : tuple(idx, element)] 
        hashmap= {}

        for idx, element in enumerate(nums):
            if element in hashmap:
                return [hashmap[element][0], idx]

            substraction = target - element
            hashmap[substraction] = (idx, element)

        