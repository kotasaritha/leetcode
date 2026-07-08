class Solution:
    def sumAndMultiply(self,s:str,queries:List[List[int]])->List[int]:
        MOD=10**9+7
        pos=[]
        digit=[]
        for i,ch in enumerate(s):
            if ch!='0':
                pos.append(i)
                digit.append(int(ch))
        m=len(digit)
        pow10=[1]*(m+1)
        for i in range(1,m+1):
            pow10[i]=(pow10[i-1]*10)%MOD
        prefsum=[0]*(m+1)
        prefhash=[0]*(m+1)
        for i in range(m):
            prefsum[i+1]=prefsum[i]+digit[i]
            prefhash[i+1]=(prefhash[i]*10+digit[i])%MOD
        def lower(x):
            l,r=0,len(pos)
            while l<r:
                mid=(l+r)//2
                if pos[mid]<x:
                    l=mid+1
                else:
                    r=mid
            return l
        def upper(x):
            l,r=0,len(pos)
            while l<r:
                mid=(l+r)//2
                if pos[mid]<=x:
                    l=mid+1
                else:
                    r=mid
            return l
        ans=[]
        for l,r in queries:
            L=lower(l)
            R=upper(r)
            if L==R:
                ans.append(0)
                continue
            length=R-L
            num=(prefhash[R]-prefhash[L]*pow10[length])%MOD
            sm=prefsum[R]-prefsum[L]
            ans.append((num*sm)%MOD)
        return ans