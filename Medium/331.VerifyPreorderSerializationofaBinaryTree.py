class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        li = preorder.split(',')
        if li[0] == '#':
            return len(li) == 1
       
        stack = []
        for i, n in enumerate(li):
            print(stack)
            if stack: 
                stack[-1][1] += 1
                if stack[-1][1] == 2:
                    stack.pop()      

            if n != '#':
                stack.append([n, 0])
            
            if not stack:
                return i == len(li) - 1
            