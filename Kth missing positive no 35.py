class Solution:
    def kthMissing(self, arr, k):
        # code here
        l=[]
        arr=set(arr)
        for i in range(1,max(arr)):
            if i not in arr:
                l.append(i)
        if k>len(l) or not l:
            return max(arr)+(k-len(l))
        return l[k-1]
