from ast import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        def recursion(substr):
            if not substr:
                return [""]

            res = []
            for i in range(1, len(substr) + 1):
                word = substr[:i]
                if word in word_set:
                    for followed_str in recursion(substr[i:]):
                        if len(followed_str):
                            res.append(word + " " + followed_str)
                        else:
                            res.append(word)

            return res 
        return recursion(s)
