from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        que = deque([(1, beginWord)])
        wordList, visited = set(wordList), set()    
        while que:
            depth, curr_word = que.popleft()

            if curr_word == endWord:
                return depth

            if curr_word in visited:
                continue

            visited.add(curr_word)

            # This is faster than loop in wordList
            for i in range(len(curr_word)): 
                for c in "abcdefghijklmnopqrstuvwxyz": 
                    next_word = curr_word[:i] + c + curr_word[i+1:]
                    if next_word in wordList:
                        que.append((depth + 1, next_word))
    
        return 0