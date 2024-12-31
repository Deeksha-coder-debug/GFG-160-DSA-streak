class Solution:
    def isValid(self,a,maxAllow,k):
        stu=1
        pages=0
        for p in a:
            if p>maxAllow:
                return False
            elif pages+p<=maxAllow:
                pages+=p
            else:
                stu+=1
                pages=p
        return stu<=k
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        if k>len(arr):
            return -1
        st=max(arr)
        end=sum(arr)
        ans=-1
        while st<=end:
            mid=st+(end-st)//2
            if self.isValid(arr,mid,k):
                ans=mid
                end=mid-1
            else:
                st=mid+1
        return ans
