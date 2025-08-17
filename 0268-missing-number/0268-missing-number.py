class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        k = 0
        while k<=len(nums):
            if k not in nums:
                return k
            k+=1

        return
