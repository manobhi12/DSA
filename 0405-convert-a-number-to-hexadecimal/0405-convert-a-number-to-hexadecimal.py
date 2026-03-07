class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        result = ""
        
        for _ in range(8):  
            digit = num & 15
            result = hex_chars[digit] + result
            num >>= 4
        
        return result.lstrip('0')