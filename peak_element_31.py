# finding peak element in array
class Solution:   
    def peakElement(self,arr):
        # Code here
        if len(arr)==1 or arr[0]>arr[1]:
            return 0
        if arr[-1]>arr[-2]:
            return len(arr)-1
        l=1
        h=len(arr)-2
        while l<=h:
            m=l+(h-l)//2
            if arr[m-1]<arr[m] and arr[m]>arr[m+1]:
                return m
            elif arr[m-1]<arr[m]<arr[m+1]:
                l=m+1
            else:
                h=m-1
        return m
