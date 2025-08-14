class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        n = len(nums)
        if n%2==0 :
            med1 = n//2
            med2 = n//2 - 1
            median = (nums[med1]+nums[med2])/2.0
        else :
            med = (n-1)//2
            median = nums[med]
        
        return median
        