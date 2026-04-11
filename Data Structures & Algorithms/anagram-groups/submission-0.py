class Solution:
    def groupAnagrams(self, s: list[str]) -> list[list[str]]:
        def r(s, y):
            o = [0] * 26
            for i, j in zip(s, y):
                o[ord(i) - ord('a')] += 1
                o[ord(j) - ord('a')] -= 1
            return o == ([0] * 26)
        h = []
        for i in range(len(s)):
            y = []
            for j in range(i, len(s)):
                if (
                    r(s[i], s[j])
                    and len(s[i]) == len(s[j])
                    and any(k == s[j] for i in h for k in i) != True
                ):
                    y.append(s[j])
            if y != []:
                h.append(y)
        return h