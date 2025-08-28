class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # peak1=0
        # for i in range(1,len(nums)-1):
        #     if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
        #         peak1=i
        # return peak1
        left,right=0,len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid]>nums[mid+1]:
                right=mid
            else:
                left=mid+1
        return left

        