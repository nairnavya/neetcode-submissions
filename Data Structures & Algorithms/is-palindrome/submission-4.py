class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left = 0
        right = len(s)-1
        s_fromleft = ""
        s_fromright = ""
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if (s[left]!=s[right]):
                print(f"s_fromleft if {s_fromleft}")
                print(f"s_fromright if {s_fromright}")
                print(f"s[left] is {s[left]} but s[right] is {s[right]}")
                print(f"s[left] is {s[left]} and s[left-1] is {s[left-1]}")
                return False

            s_fromleft = s_fromleft + s[left]
            s_fromright = s_fromright + s[right]
            
            left += 1
            right -= 1
        print(f"s_fromleft if {s_fromleft}")
        print(f"s_fromright if {s_fromright}")
        return True
            
