class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}
        for i, num in enumerate(nums):
            if num not in seen :
                seen[num] = 1
            else:
                seen[num] += 1
            
        for key, value in seen.items():
            if value > len(nums)/2 :
                return key
            
        

        