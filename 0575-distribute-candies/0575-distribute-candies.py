class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        unique_types = len(set(candyType))
        return min(unique_types, len(candyType) // 2)       