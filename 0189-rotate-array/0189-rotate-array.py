class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x=0
        while x<k :
            last_num = nums.pop()
            nums.insert(0, last_num)
            x+=1
        