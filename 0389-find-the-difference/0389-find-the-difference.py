class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        for i in t:
            d[i]=d.get(i,0)+1
        for i in s:
            if i in d:
                d[i]-=1
        c=""
        for i in d:
            if d[i]==1:
                c+=i
        return c


        