class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ""

        short = min((len(word1)), (len(word2)))

        for i in range(short):
            new += word1[i]
            new += word2[i]

        new += word1[short:]
        new += word2[short:]

        return new
    



