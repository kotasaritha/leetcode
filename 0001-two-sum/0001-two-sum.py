class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum=0
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                sum=nums[i]+nums[j]
                if sum==target:
                    l.append(i)
                    l.append(j)
        return l
                    

        