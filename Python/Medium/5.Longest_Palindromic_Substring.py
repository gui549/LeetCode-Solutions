class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = (0, 0)
        for i in range(len(s)):
            r = i
            while r < len(s) and s[i] == s[r]:
                r += 1

            l = i - 1
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            
            if ans[1] - ans[0] < r - l - 2:
                ans = (l + 1, r - 1)

        return s[ans[0]:ans[1]+1]

        """
        xbbcbbz        
         llirr      
        """