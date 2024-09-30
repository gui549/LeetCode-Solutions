class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = dict()
        def recursion(s):
            if not s:
                return True
            
            if s in cache:
                return cache[s]

            for word in wordDict:
                index = s.find(word)
                if index == -1:
                    continue
                if recursion(s[:index]) and recursion(s[index + len(word):]):
                    cache[s] = True
                    return True

            cache[s] = False
            return False
            
        return recursion(s)