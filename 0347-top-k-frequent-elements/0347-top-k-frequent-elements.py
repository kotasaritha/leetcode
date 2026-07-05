class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        result=dict(sorted(d.items(),key=lambda x:x[1]))
        l=[]
        for i in result:
            l.append(i)
        ans=[]
        for i in range(k):
                ans.append(l[len(result)-1-i])
        return ans
        
        