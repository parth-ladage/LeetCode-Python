class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxEnd = nums[0]
        minEnd = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            n = nums[i]
            if n<0:
                maxEnd, minEnd = minEnd, maxEnd
            maxEnd = max(n, maxEnd*n)
            minEnd = min(n, minEnd*n)

            result = max(maxEnd,result)

        return result
        