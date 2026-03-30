class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        freq = {}
        first = {}
        last = {}
        
        for i, num in enumerate(nums):
            if num not in first:
                first[num] = i
            last[num] = i
            freq[num] = freq.get(num, 0) + 1
        
        degree = max(freq.values())
        min_length = float('inf')
        
        for num in freq:
            if freq[num] == degree:
                length = last[num] - first[num] + 1
                min_length = min(min_length, length)
        
        return min_length     