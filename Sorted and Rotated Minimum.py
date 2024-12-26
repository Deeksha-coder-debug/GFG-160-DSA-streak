class Solution:
    def findMin(self, arr):
        #complete the function here
        if len(arr)==1:
            return arr[0]
        m=float('inf')
        for i in range(1,len(arr)):
            if arr[i]>=arr[i-1] and arr[i-1]<m:
                m=arr[i-1]
            elif arr[i]<m: 
                m=arr[i]
        return m
