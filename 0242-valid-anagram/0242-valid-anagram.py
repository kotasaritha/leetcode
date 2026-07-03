class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1={}
        d2={}
        for key in s:
            d1[key]=d1.get(key,0)+1
        for key in t:
            d2[key]= d2.get(key,0)+1
        if d1==d2:
            return True
        else:
            return False          
        