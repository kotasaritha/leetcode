class Solution:
    def alternateDigitSum(self, n: int) -> int:
        l=[]
        sum=0
        while n>0:
            d=n%10
            l.append(d)
            n=n//10
        l.reverse()
        for i in range(len(l)):
            if i%2==0:
                sum+=l[i]
                
            else:
                sum-=l[i]
        return sum
        