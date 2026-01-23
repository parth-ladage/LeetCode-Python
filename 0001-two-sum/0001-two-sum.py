class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # n = len(nums)
        # for i in range(n):
        #     for j in range(1,n):
        #         if nums[i]+nums[j] == target :
        #             return [i,j]
        seen = {}
        for index, num in enumerate(nums):
            comp = target - num
            if comp in seen:
                return [seen[comp], index]
            else:
                seen[num] = index
        return []
        