class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nums=temperatures
        res=[0]*len(nums)
        st=[]
        for i in range(len(nums)-1,-1,-1):
            ele=nums[i]
            while st and ele>=nums[st[-1]]:
                st.pop()
            if st:
                res[i]=st[-1]-i
            else:
                res[i]=0
            st.append(i)
        return res
        