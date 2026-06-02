class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        substring = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1
            
            char_set.add(s[r])

            substring = max(substring, r-l+1)
        return substring
        