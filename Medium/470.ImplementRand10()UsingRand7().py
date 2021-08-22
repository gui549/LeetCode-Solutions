class Solution:
    def rand10(self):
        total = (rand7() - 1) * 7 + (rand7() - 1)
        while total >= 40:
            total = (rand7() - 1) * 7 + (rand7() - 1)
        return (total % 10) + 1