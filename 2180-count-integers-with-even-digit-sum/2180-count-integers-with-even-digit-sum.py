class Solution:
    def countEven(self, num: int) -> int:
        sum=0
        c=0
        for i in range(1,num+1):
            if i<10 and i%2==0:
                c+=1
            else:
                s=0
                while i>0:
                    d=i%10
                    s+=d
                    i=i//10
                if s%2==0:
                    c+=1
        return c
                