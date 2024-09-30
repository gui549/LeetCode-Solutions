# class Solution:
#     def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
#         wordList1 = sentence1.split(" ")
#         wordList2 = sentence2.split(" ")

#         def check(li1, li2):
#             res1, res2, i, j = [], [], 0, 0
#             for k in range(len(li2)):
#                 while i < len(li1):
#                     if li2[k] == li1[i]:
#                         res1.append(i)
#                         i += 1
#                         break
#                     i += 1
                
#                 while j < len(li1):
#                     if li2[~k] == li1[~j]:
#                         res2.append(~j)
#                         j += 1
#                         break
#                     j += 1
                
#             if len(res1) != len(li2) and len(res2) != len(li2):
#                 return False

#             indices1 = [i for i in range(len(li1))]
#             for i in res1[::-1]:
#                 indices1.pop(i)

#             indices2 = [i for i in range(len(li1))]
#             for i in res2[::-1]:
#                 indices2.pop(i)

#             ans1, ans2 = True, True
#             for i in range(len(indices1) - 1):
#                 if indices1[i + 1] - indices1[i] > 1:
#                     ans1 = False
#                     break

#             for i in range(len(indices2) - 1):
#                 if indices2[i + 1] - indices2[i] > 1:
#                     ans2 = False
#                     break

#             return ans1 or ans2

#         if len(wordList1) >= len(wordList2):
#             return check(wordList1, wordList2)
#         else:
#             return check(wordList2, wordList1)

# a = Solution()
# print(a.areSentencesSimilar("A", "a A b A"))

from collections import deque

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = deque(sentence1.split())
        s2 = deque(sentence2.split())
        if (len(s1) > len(s2)):        
            s1, s2 = s2, s1
        while(s1): 
            if (s2[0] == s1[0]):
                s2.popleft()
                s1.popleft()
            elif (s2[-1] == s1[-1]):
                s2.pop()
                s1.pop()
            else:
                return(False)            
        return(True)