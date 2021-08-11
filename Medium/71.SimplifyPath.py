class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        order = []
        for dir in dirs:
            if dir == '.' or dir == '':
                continue
            elif dir == '..':
                if order:
                    order.pop()
            else:
                order.append(dir)
        print(order)
        return "/" + "/".join(order)

a = Solution()
a.simplifyPath("/home/")