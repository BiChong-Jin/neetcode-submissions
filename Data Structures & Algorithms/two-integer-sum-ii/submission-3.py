class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            pivot = numbers[i]
            #if abs(pivot) > abs(target) and target != 0:
                #break
            for j in range(i+1, len(numbers)):
                curr = numbers[j]
                if curr + pivot == target:
                    return [i+1, j+1]
                elif curr + pivot < target:
                    continue
                else:
                    break
