class Solution:

    def kthElement(self, a, b, k):
        res=[]
        i=0
        j=0
        n=len(a)
        m=len(b)
        while i<n and j<m:
            if a[i]<=b[j]:
                res.append(a[i])
                i+=1
            else:
                res.append(b[j])
                j+=1
        while i<n:
            res.append(a[i])
            i+=1
        while j<m:
            res.append(b[j])
            j+=1
        return res[k-1]
