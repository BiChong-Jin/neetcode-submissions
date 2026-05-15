class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        queue = deque()

        for idx, element in enumerate(temperatures):
            while queue and element > queue[-1][0]:
                temp, id= queue.pop()
                res[id] = idx - id

            queue.append((element, idx))


        return res