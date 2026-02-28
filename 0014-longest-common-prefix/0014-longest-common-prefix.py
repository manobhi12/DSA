class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""
        
        # Take first string as reference
        for i in range(len(strs[0])):
            
            # Compare character with other strings
            for s in strs:
                # If index out of range OR mismatch found
                if i >= len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]
        
        return strs[0]