class Solution:
    def isValid(self,s,minAllow,k):
        cow=1
        lastPos=s[0]
        for i in s:
            if((i-lastPos)>=minAllow):
                cow+=1
                lastPos=i
            if cow==k:
                return True
        return False
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        st=1
        ans=0
        end=max(stalls)-min(stalls)
        while st<=end:
            mid=st+(end-st)//2
            if self.isValid(stalls,mid,k):
                ans=mid
                st=mid+1
            else:
                end=mid-1
        return ans
