class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        for i in tokens:
            if i =="+":
                l.append(l.pop()+l.pop())
            elif i=="-":
                second=l.pop()
                first=l.pop()
                l.append(first-second)
            elif i=="*":
                l.append(l.pop()*l.pop())
            elif i=="/":
                second=l.pop()
                first=l.pop()
                l.append(int(first/second))
            else:
                l.append(int(i))
        return l[0]