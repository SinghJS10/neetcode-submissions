from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq = Counter(nums)
        sorted_items = sorted(freq.items(), key = lambda x:x[1], reverse = True)
        for key, value in sorted_items[:k]:
            result.append(key)
        return result
            
        