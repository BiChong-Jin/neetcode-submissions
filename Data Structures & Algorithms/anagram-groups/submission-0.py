class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for element in strs:
            counts = [0] * 26

            if element == "":
                hashmap[tuple(counts)].append(element)
            
            else:
                for char in element:
                    counts[ord(char) - ord("a")] += 1
                hashmap[tuple(counts)].append(element)
            
        return list(hashmap.values())