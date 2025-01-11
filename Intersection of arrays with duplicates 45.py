class Solution:
    def intersectionWithDuplicates(self, a, b):
        # code here
        a=set(a)
        b=set(b)
        l=[]
        for i in a:
            if i in b:
                l.append(i)
        return l
