class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        dup = True
        if (ax1 > bx2 or ay1 > by2) and (ax2 < bx1 or ay2 < by1):
            dup = False
        point1 = (bx1 if bx1 >= ax1 else ax1, by1 if by1 >= ay1 else ay1)
        point2 = (bx2 if bx2 <= ax2 else ax2, by1 if by1 >= ay1 else ay1)
        point3 = (bx1 if bx1 <= ax1 else ax1, by2 if by2 <= ay2 else ay2)
        point4 = (bx2 if bx2 <= ax2 else ax2, by2 if by2 <= ay2 else ay2) 
        dupArea = (point2[0] - point1[0]) * (point4[1] - point1[1])
        if dup:
            return abs(ax2 - ax1) * abs(ay2 - ay1) + abs(bx2 - bx1) * abs(by2 - by1) - dupArea
        else:
            return abs(ax2 - ax1) * abs(ay2 - ay1) + abs(bx2 - bx1) * abs(by2 - by1) 

a = Solution()
print(a.computeArea(-2,-2,2,2,-3,-3,3,-1))
