class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        key = {
            "}":"{",
            ")":"(",
            "]":"["
        }

        opening = ["(", "{", "["]
        stack = []

        for char in s:
            if char in opening:
                stack.append(char)
            else:
                if len(stack) == 0 or key[char] != stack[-1]:
                    return False
                        
                stack.pop()
            
        return len(stack)==0