class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        l=[]
        for i in range(len(nums)):
            n=str(nums[i])
            for j in range(len(n)):
                l.append(int(n[j]))
        return l