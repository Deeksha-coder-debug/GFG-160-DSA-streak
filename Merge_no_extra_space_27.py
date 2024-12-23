class Solution:
    def mergeArrays(self, a, b):
        # code here
        n=len(a)
        m=len(b)
        j=n-1
        k=0
        while k<m and j>=0 and b[k]<a[j]:
            a[j],b[k]=b[k],a[j]
            j-=1
            k+=1
        a.sort()
        b.sort()
