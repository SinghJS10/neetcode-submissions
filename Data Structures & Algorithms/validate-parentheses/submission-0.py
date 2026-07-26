class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []
        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack or stack.pop() != mapping[ch]:
                    return False
        return len(stack) == 0
        
        