from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        res = [""]
        d = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", 
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

        for digit in digits:
            news = []
            for s in res:
                for ch in d[digit]:
                    news.append(s + ch)
            res = news

        return res