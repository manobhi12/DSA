class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_value = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman_to_value[s[i]] < roman_to_value[s[i + 1]]:
                total -= roman_to_value[s[i]]
            else:
                total += roman_to_value[s[i]]

        return total
        