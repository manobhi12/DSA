class Solution:
    def countLargestGroup(self, n: int) -> int:
        from collections import defaultdict
        
        groups = defaultdict(int)
        

        for num in range(1, n + 1):
            digit_sum = sum(map(int, str(num)))
            groups[digit_sum] += 1
        

        max_size = max(groups.values())
        

        return sum(1 for size in groups.values() if size == max_size)