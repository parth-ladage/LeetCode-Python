class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        seen = defaultdict(int)
        for i in nums :
            seen[i] += 1

        for i, count in seen.items():
            if count == 1 :
                return i
        
        return
            


