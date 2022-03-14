from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split()
        dict_order_by_len = sorted(dictionary, key=lambda k:len(k))

        for i in range(len(words)):
            for key in dict_order_by_len:
                if words[i].startswith(key):
                    words[i] = key

        return " ".join(words)

