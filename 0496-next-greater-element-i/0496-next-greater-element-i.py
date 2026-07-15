class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=[]
        d={}
        for i in range(len(nums2)-1,-1,-1):
            ele=nums2[i]
            while l and ele>l[-1]:
                l.pop()
            if len(l)==0:
                d[ele]=-1
            else:
                d[ele]=l[-1]
            l.append(ele)
        l1=[]
        for i in nums1:
           
            l1.append(d[i])
         
        return l1



        