class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for index, num in enumerate(nums):
            if num in seen:
                seen[num]+=1
                if seen[num]>1:
                    return True
                else:
                    return False
            else:
                seen[num]=1
        return False