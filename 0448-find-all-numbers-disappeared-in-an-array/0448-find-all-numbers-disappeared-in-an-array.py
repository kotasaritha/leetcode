class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s=set(nums)
        l=[]
        for i in range(1,len(nums)+1):
            if i not in s:
                l.append(i)
        return l
        