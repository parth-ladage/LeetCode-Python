class Solution:
    def checkRecord(self, s: str) -> bool:
        A=0
        strList = list(s)
        for i in range(len(strList)):
            if strList[i]=='A':
                A+=1
                if A>=2:
                    return False

            if i>=2 and strList[i]=='L' and strList[i-1]=='L' and strList[i-2]=='L':
                return False

        return True

            

        