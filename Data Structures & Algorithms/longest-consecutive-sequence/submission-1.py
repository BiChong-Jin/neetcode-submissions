class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        turn the given array into a hashset for constant lookup time O(1)

        loop through the array, keep checking if the current element - 1 is in the array;
        if it is: so the sequence is still building -> len(sequence) + 1
        if it is not in the array: this current element is a new starting point of a sequence, end previous 
        """
        set_nums = set(nums)
        res = 0

        for num in nums:
            if num - 1 not in set_nums:
                curr_starting_num = num
                curr_res = 1
                while curr_starting_num + 1 in set_nums:
                    curr_res += 1
                    curr_starting_num += 1

                res = max(res, curr_res)
            else:
                continue

        return res