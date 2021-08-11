class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        li = [[p1, p2, p3, p4], [p1, p2, p4, p3],
            [p1, p3, p2, p4], [p1, p3, p4, p2],
            [p1, p4, p2, p3], [p1, p4, p3, p2]]

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def innerProduct(p1, p2, p3):
            return (p1[0] - p2[0]) * (p1[0] - p3[0]) + \
            (p1[1] - p2[1]) * (p1[1] - p3[1])

        for [p1, p2, p3, p4] in li:
            if dist(p1, p2) != 0 and dist(p1, p2) == dist(p2, p3) == dist(p3, p4) == dist(p4, p1) and \
                innerProduct(p1, p2, p4) == innerProduct(p2, p3, p1) == innerProduct(p3, p2, p4) == innerProduct(p4, p3, p1) == 0:
                return True

        return False