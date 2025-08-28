class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        result=0
        for i in range(len(nums)):
            result = result^nums[i]
        
        return result

        