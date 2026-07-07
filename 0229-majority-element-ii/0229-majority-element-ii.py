class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d={}
        s=len(nums)/3
        for i in nums:
            d[i]=d.get(i,0)+1
        l=[]
        for i in d:
            if d[i]>s:
                l.append(i)
        return l
                       