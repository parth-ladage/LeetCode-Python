class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = abs(x)
        rev = 0
        while temp != 0:
            rev = rev*10+ temp%10
            temp=temp//10
        
        if x<0: rev=-rev
        if rev > 2**31 - 1 or rev < -2**31:
            return 0

        return rev