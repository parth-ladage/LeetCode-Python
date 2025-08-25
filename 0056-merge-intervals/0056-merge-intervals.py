class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        n = len(intervals)
        intervals.sort()
        for i in range(n):
            start = intervals[i][0]
            end = intervals[i][1]
            if len(res)!=0 and end<=res[-1][1]:
                continue
            for j in range(i+1, n):
                if intervals[j][0]<=end:
                    end = max(end, intervals[j][1])
                else:
                    break
            res.append([start,end])

        return res
        