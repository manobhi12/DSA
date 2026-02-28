class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        # Mapping closing brackets to opening brackets
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            # If opening bracket, push to stack
            if char in mapping.values():
                stack.append(char)
            
            # If closing bracket
            elif char in mapping:
                # If stack empty OR top doesn't match
                if not stack or stack[-1] != mapping[char]:
                    return False
                stack.pop()
        
        # Valid only if stack is empty
        return len(stack) == 0