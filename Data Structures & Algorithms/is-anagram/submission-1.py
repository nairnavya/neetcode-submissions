class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = sorted(s)
        list_t = sorted(t)
        
        print("s is", list_s)
        print("t is", list_t)

        if len(list_s) != len(list_t):
            return False
            
        for i in range(len(list_s)):
            if list_s[i] != list_t[i]:
                return False
        
        return True
        