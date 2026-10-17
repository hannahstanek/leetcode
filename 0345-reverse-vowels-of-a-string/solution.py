class Solution:
    def reverseVowels(self, s: str) -> str:
        key = []
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        for i in range(len(s)):
            if s[i] in vowel:
                key += s[i]

        key.reverse()
        back = key
        a = 0
        letters = list(s)

        for i in range(len(letters)):
            if letters[i] in vowel:
                letters[i] = back[a]
                a += 1
        return "".join(letters)

        return s            
