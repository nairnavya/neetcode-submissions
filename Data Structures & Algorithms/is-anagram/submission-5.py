class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for letter in s:
            if letter not in s_map:
                s_map[letter] = 1
            else:
                s_map[letter] += 1

        for letter in t:
            if letter not in t_map:
                t_map[letter] = 1
            else:
                t_map[letter] += 1

        for alphabet in s_map:
            if (alphabet not in t_map or s_map[alphabet] != t_map[alphabet]):
                return False
        for alphabet in t_map:
            if (alphabet not in s_map or t_map[alphabet] != s_map[alphabet]):
                return False
        return True

        