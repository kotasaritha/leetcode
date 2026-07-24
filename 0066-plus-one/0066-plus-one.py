class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sum=0
        l=[]
        for i in range(len(digits)):
            sum=sum*10+digits[i]
        sum=sum+1
        s=str(sum)
        for i in s:
            l.append(int(i))
        return l    