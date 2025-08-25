class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                seen[num]+=1
            else:
                seen[num]=1
        
        for num in seen:
            if seen[num] > len(nums)/3 :
                res.append(num)
            
        return res

        