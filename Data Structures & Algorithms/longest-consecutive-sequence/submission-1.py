class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxLength = 0
        if len(nums) == 0:
            return 0
        numSet = set(nums)
        for num in numSet:
            if num - 1 not in numSet:
                current = num
                length = 1
                while current + 1 in numSet:
                    current += 1
                    length += 1
                maxLength = max(maxLength, length)
        return maxLength
