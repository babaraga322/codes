class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        count = [0] * (n+1)
        for i in nums:
            if count[i] == 0:
                count[i] = 1
            else:
                return i