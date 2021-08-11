from typing import List
from collections import defaultdict

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        # ordered = [(scores[i], ages[i]) for i in range(len(scores))]
        
        # ordered = sorted(ordered, key=lambda s: s[0])
        ordered = sorted(zip(scores, ages), key=lambda s: s[0])
        ordered = sorted(ordered, key=lambda s: s[1])

        answer = 0
        dp = [ordered[i][0] for i in range(len(ordered))]
        for i in range(len(dp)):
            for j in range(i):
                if ordered[i][0] >= ordered[j][0]:
                    dp[i] = max(dp[i], dp[j] + ordered[i][0])
            answer = max(answer, dp[i])

        return answer        

a = Solution()
print(a.bestTeamScore([648,374,437,279,258,223,225,802,744,537,60,524,991,20,462,359,208,577,515,734,233,217,548,947,511,653,237,315,824,480,741],[16,55,21,48,23,7,27,37,99,33,26,76,84,1,45,78,84,89,64,99,97,28,23,91,32,97,68,84,57,7,65]))
