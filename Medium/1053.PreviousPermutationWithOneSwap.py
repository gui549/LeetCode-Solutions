from typing import List

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 2, -1, -1):
            li = [j for j in range(i + 1, len(arr)) if arr[j] < arr[i]]
            print(i, li)
            if li:
                j = max(li, key=lambda x: arr[x])
                arr[i], arr[j] = arr[j], arr[i]
                return arr

        return arr

a = Solution()
print(a.prevPermOpt1([1, 1, 5]))