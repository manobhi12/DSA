from collections import Counter

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        count = Counter(arr1)
        result = []
        

        for num in arr2:
            result.extend([num] * count[num])
            count.pop(num)
        

        remaining = []
        for num, freq in count.items():
            remaining.extend([num] * freq)
        
        result.extend(sorted(remaining))
        
        return result