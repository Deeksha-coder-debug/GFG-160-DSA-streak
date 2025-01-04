class Solution:
    def matSearch(self, mat, x):
        # Complete this function
        for i in mat:
            st=0
            end=len(i)-1
            while st<=end:
                mid=st+(end-st)//2
                if i[mid]==x:
                    return True
                elif i[mid]<x:
                    st=mid+1
                else:
                    end=mid-1
        return False
