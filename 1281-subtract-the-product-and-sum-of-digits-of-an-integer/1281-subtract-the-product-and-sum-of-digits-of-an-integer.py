class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digitSum=0
        digitPro=1
        while n>0:
            digit=n%10
            n=n//10
            digitSum+=digit
            digitPro*=digit

        return digitPro-digitSum

        