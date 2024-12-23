class Solution:
    def minRemoval(self, intervals):
        # Code here
        rem=0
        intervals.sort()
        end=intervals[0][1]
        for i in range(1,len(intervals)):
            if(intervals[i][0]<end):
                rem+=1
                end=min(intervals[i][1],end)
            else:
                end=intervals[i][1]
        return rem
