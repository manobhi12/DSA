from collections import defaultdict

class Solution:
    def findFrequentTreeSum(self, root):

        freq = defaultdict(int)

        def dfs(node):

            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            total = node.val + left_sum + right_sum

            freq[total] += 1

            return total

        dfs(root)

        max_freq = max(freq.values())

        result = []

        for s in freq:
            if freq[s] == max_freq:
                result.append(s)

        return result     