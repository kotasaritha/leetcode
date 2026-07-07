class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=0
        sum=0
        while n>0:
            d=n%10
            if d!=0:
                x=x*10+d
            n=n//10
        ans=0
        while x>0:
            d=x%10
            sum=sum+d
            ans=ans*10+d
            x=x//10
        return ans*sum