import random

class Solution:

    def __init__(self, nums):

        self.original = nums[:]
        self.nums = nums[:]

    def reset(self):

        self.nums = self.original[:]
        return self.nums

    def shuffle(self):

        arr = self.nums[:]
        n = len(arr)


        for i in range(n):

            rand_idx = random.randint(i, n - 1)

            arr[i], arr[rand_idx] = arr[rand_idx], arr[i]

        return arr