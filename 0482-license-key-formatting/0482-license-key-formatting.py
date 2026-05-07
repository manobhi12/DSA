class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:


        cleaned = s.replace('-', '').upper()

        n = len(cleaned)

        result = []

        first_group = n % k

        index = 0


        if first_group > 0:
            result.append(cleaned[:first_group])
            index = first_group

 
        while index < n:
            result.append(cleaned[index:index + k])
            index += k

        return '-'.join(result)