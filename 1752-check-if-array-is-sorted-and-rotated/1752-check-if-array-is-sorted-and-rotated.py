class Solution:
    def check(self, nums: List[int]) -> bool:
        while nums != sorted(nums) :
            if nums[0] < nums[len(nums)-1]:
                return False
            else:
                last_element = nums.pop()
                nums.insert(0, last_element)

        return True

        