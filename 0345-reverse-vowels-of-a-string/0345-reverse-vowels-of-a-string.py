class Solution:
    def reverseVowels(self, s: str) -> str:
        l1=["A","E","I","O","U","a","e","i","o","u"]
        l=[]
        for i in s:
            l.append(i)
        i=0
        j=len(s)-1
        while i<j:
            if l[i] in l1 and l[j] in l1:
                temp=l[i]
                l[i]=l[j]
                l[j]=temp
                i+=1
                j-=1
            elif l[i] not in l1:
                i+=1
            elif l[j] not in l1:
                j-=1
        result="".join(l)
        return result
        
         
        