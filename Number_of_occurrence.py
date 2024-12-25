class Solution:
    def countFreq(self, arr, target):
        #code here
        i=0
        count=0
        while i<len(arr):
            if(arr[i]==target):
                count+=1
            i+=1
        return count
