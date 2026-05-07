from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals):

        n = len(intervals)

     
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))

        start_values = [x[0] for x in starts]

        result = []

        for start, end in intervals:

         
            idx = bisect_left(start_values, end)

            if idx == n:
                result.append(-1)
            else:
                result.append(starts[idx][1])

        return result