class Solution:
    def maximumGap(self, nums):
        n = len(nums)
        if n < 2:
            return 0
        
        mn, mx = min(nums), max(nums)
        if mn == mx:
            return 0
        
        size = max(1, (mx - mn) // (n - 1))
        count = (mx - mn) // size + 1
        
        bucket_min = [float('inf')] * count
        bucket_max = [float('-inf')] * count
        
        for num in nums:
            idx = (num - mn) // size
            bucket_min[idx] = min(bucket_min[idx], num)
            bucket_max[idx] = max(bucket_max[idx], num)
        
        prev = mn
        res = 0
        
        for i in range(count):
            if bucket_min[i] == float('inf'):
                continue
            res = max(res, bucket_min[i] - prev)
            prev = bucket_max[i]
        
        return res
        