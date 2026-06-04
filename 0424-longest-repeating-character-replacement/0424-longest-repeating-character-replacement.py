class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        maxFrequency = 0
        longest = 0

        for r in range(len(s)):
            char = s[r]
            count[char] = count.get(char, 0) + 1

            maxFrequency = max(maxFrequency, count[char])

            windowSize = r-l+1

            if windowSize-maxFrequency > k:
                leftChar = s[l]
                count[leftChar] -= 1
                l += 1

            longest = max(longest, r-l+1)

        return longest
        