class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from operator import itemgetter

        counts = Counter(nums)
        # {element : apperence}
        list_counts = list(counts.items())
        list_counts.sort(key=itemgetter(1), reverse=True)
        top_k = list_counts[:k]
        return [e for e, _ in top_k]
        